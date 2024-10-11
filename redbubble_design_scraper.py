import os
import argparse
import csv
from dotenv import load_dotenv
from scrappeycom.scrappey import Scrappey


load_dotenv(".env")


class RedbubbleScraper:
    def __init__(self, output_dir: str):
        self.scrappey = Scrappey(os.getenv("SCRAPPEY_API_KEY"))
        self.output_dir = output_dir

    def _get(self, request_payload: dict) -> dict | None:
        tries = 0
        while tries < 3:
            try:
                res = self.scrappey.get(request_payload)
                if res.get("error", None):
                    raise Exception(res.get("error"))
                return res
            except Exception as error:
                print(f"An error occurred while fetching product details: {error}")
                tries += 1
        return None

    def _write_to_csv(self, image_urls: list[str]) -> str | None:
        try:
            # Ensure output directory exists
            os.makedirs(self.output_dir, exist_ok=True)

            # Create CSV file
            file_path = os.path.join(self.output_dir, "image_links.csv")

            with open(file_path, "w", newline="") as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(["Image URL"])  # Write header
                for url in image_urls:
                    writer.writerow([url])

            return file_path
        except IOError as error:
            print(f"An error occurred while writing to CSV: {error}")
            return None

    def get_designs_from_shop(self, shop_url: str):
        request_payload = {
            "cmd": "request.get",
            "url": shop_url,
            "browser": [{"name": "chrome"}],
            "noDriver": True,
            "cssSelector": '[data-testid="ds-box"] img',
            "customAttribute": "src",
        }
        res = self._get(request_payload)
        solution = res.get("solution", None)
        if solution and solution.get("statusCode", None) == 200:
            images = [
                img
                for img in solution.get("cssSelector", [])
                if img.startswith("https://ih1.redbubble.net")
            ]
            csv_path = self._write_to_csv(images)
            if csv_path:
                print(f"Image links have been written to {csv_path}")
            else:
                print("Failed to write image links to CSV")


def main():
    parser = argparse.ArgumentParser(description="Scrape designs from a Redbubble shop")
    parser.add_argument(
        "--shop", required=True, help="URL of the Redbubble shop to scrape"
    )
    parser.add_argument(
        "--output", default="output", help="Output directory for CSV file"
    )
    args = parser.parse_args()

    scraper = RedbubbleScraper(output_dir=args.output)
    scraper.get_designs_from_shop(args.shop)


if __name__ == "__main__":
    main()
