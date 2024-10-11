# Redbubble Design Scraper

This Python script allows you to scrape design images from a Redbubble shop. It uses the Scrappey API to fetch image URLs and then downloads the images to a specified output directory.

## Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

## Setup

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/redbubble-design-scraper.git
cd redbubble-design-scraper
```

### 2. Create a virtual environment

#### On Linux and macOS:
```bash
python3 -m venv venv
source venv/bin/activate
```

#### On Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up the Scrappey API key

1. Go to [https://app.scrappey.com/](https://app.scrappey.com/) and sign up for an account.
2. Once logged in, navigate to the API section to obtain your API key.
3. Create a `.env` file in the project root directory and add your API key:

```SCRAPPEY_API_KEY=your_scrappey_api_key```


## Usage

To run the script, use the following command after activating your venv:
```bash
python redbubble_design_scraper.py --shop <shop_url> --output <output_directory>
```

- `<shop_url>`: The URL of the Redbubble shop you want to scrape (required)
- `<output_directory>`: The directory where images will be saved (optional, defaults to "output")

Example:
```bash
python redbubble_design_scraper.py --shop https://www.redbubble.com/people/artistname/shop --output downloaded_designs
```

This will scrape design images from the specified Redbubble shop and save them in the "downloaded_designs" directory.

## Notes

- The script will create the output directory if it doesn't exist.
- Images are downloaded with their original filenames from Redbubble.
- The script will attempt to fetch data up to 3 times in case of errors.

## Troubleshooting

If you encounter any issues:

1. Ensure your Scrappey API key is correct and properly set in the `.env` file.
2. Check your internet connection.
3. Verify that the Redbubble shop URL is valid and accessible.

For any other problems, please open an issue on the GitHub repository.
