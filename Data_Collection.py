import os
import zipfile
import logging
from kaggle.api.kaggle_api_extended import KaggleApi

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Constants
COMPETITION_NAME = 'tabular-playground-series-oct-2022'
DOWNLOAD_DIR = 'C:\\Users\\march\\Downloads\\kaggle_data'
ZIP_FILE_NAME = f'{COMPETITION_NAME}.zip'

def authenticate_kaggle_api():
    """Authenticate with the Kaggle API using KaggleApi class."""
    try:
        api = KaggleApi()
        api.authenticate()
        logging.info("Authenticated with Kaggle API successfully.")
        return api
    except Exception as e:
        logging.error(f"Failed to authenticate with Kaggle API: {e}")
        raise

def download_competition_data(api, competition, download_path):
    """Download competition data from Kaggle."""
    try:
        api.competition_download_files(competition, path=download_path)
        logging.info(f"Downloaded competition data for {competition} to {download_path}")
    except Exception as e:
        logging.error(f"Failed to download competition data: {e}")
        raise

def extract_zip_file(zip_file_path, extract_to):
    """Extract the contents of a zip file to the specified directory."""
    try:
        with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            zip_ref.extractall(extract_to)
        logging.info(f"Extracted zip file {zip_file_path} to {extract_to}")
    except zipfile.BadZipFile as e:
        logging.error(f"Error extracting zip file: {e}")
        raise
    except Exception as e:
        logging.error(f"An unexpected error occurred while extracting the zip file: {e}")
        raise

def extract_requests():
    """Extract data getting the url."""
    import json
    import requests

    try:
        # Load your Kaggle API token
        with open('C:\\Users\\march\\.kaggle\\kaggle.json', 'r') as file:
            kaggle_token = json.load(file)

        # Authenticate with Kaggle
        KAGGLE_USERNAME = kaggle_token['username']
        KAGGLE_KEY = kaggle_token['key']

        # Dataset or competition URL
        DATASET_URL = 'https://storage.googleapis.com/kaggle-competitions-data/kaggle-v2/33110/4321918/bundle/archive.zip?GoogleAccessId=web-data@kaggle-161607.iam.gserviceaccount.com&Expires=1722632398&Signature=ChSSX8%2BLs0jXbdNkQtbnaFomvmOCdtKw%2FMpDyRtOLdtPKggNdZiwbgSnm%2BCLPr4m39aQ5ULes%2FmxtLW7iSHfvgLTGjMi%2BtuF1SHDY97KJZS0bKTnaTOJizrLyiJtAzvBAfnOo6mmPpHspItF8Nt0Fqas7cqciNrU3%2BQshToetXUVapy1JecK5wlL1riKyEq1EcezGfPEIW94opmxQWB4LB0vKf3GdrL5ibsNiJTpwU8K%2BIEOJA6Vjk1oQLbq4yPpICyUkorg3gBrIHS3MGHxp4u8%2BnjakKuuS%2F4xsCtegLX4yt%2BA6KdgBFb0hr%2Fys%2BD17zJyuY%2B67gzHDEwRpbLc2A%3D%3D&response-content-disposition=attachment%3B+filename%3Dtabular-playground-ser'

        # Make the request to download the dataset
        response = requests.get(DATASET_URL, auth=(KAGGLE_USERNAME, KAGGLE_KEY))

        # Save the downloaded content to a file
        with open('dataset.zip', 'wb') as file:
            file.write(response.content)

        logging.info("Dataset downloaded successfully!")
    except FileNotFoundError as e:
        logging.error(f"File not found: {e}")
        raise
    except requests.RequestException as e:
        logging.error(f"Request failed: {e}")
        raise
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        raise

def main():
    """Main function to download and extract Kaggle competition data."""
    try:
        # Authenticate with Kaggle API
        api = authenticate_kaggle_api()

        # Create directory to store downloaded files
        os.makedirs(DOWNLOAD_DIR, exist_ok=True)
        logging.info(f"Created directory {DOWNLOAD_DIR}")

        # Download competition data
        download_competition_data(api, COMPETITION_NAME, DOWNLOAD_DIR)

        # Extract downloaded zip file
        zip_file_path = os.path.join(DOWNLOAD_DIR, ZIP_FILE_NAME)
        extract_zip_file(zip_file_path, DOWNLOAD_DIR)

        logging.info(f"Downloaded and extracted files to {DOWNLOAD_DIR}")
    except Exception as e:
        logging.error(f"An error occurred in the main function: {e}")

if __name__ == '__main__':
    extract_requests()
    main()
