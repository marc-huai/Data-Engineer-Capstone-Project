import os
import zipfile
import logging
from kaggle.api.kaggle_api_extended import KaggleApi
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
import requests

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class DataAcquisition:
    def __init__(self, competition_name, download_dir):
        self.competition_name = competition_name
        self.download_dir = download_dir
        self.api = KaggleApi()
        self.zip_file_path = os.path.join(download_dir, f'{competition_name}.zip')  # Define zip file path

    def authenticate(self):
        """Authenticate with Kaggle API."""
        try:
            self.api.authenticate()
            logging.info("Authenticated with Kaggle API successfully.")
        except Exception as e:
            logging.error(f"Failed to authenticate with Kaggle API: {e}")
            raise

    def download_data(self):
        """Download data from Kaggle competition if not already downloaded."""
        try:
            # Check if the file already exists
            if not os.path.exists(self.zip_file_path):
                self.api.competition_download_files(self.competition_name, path=self.download_dir)
                logging.info(f"Downloaded competition data for {self.competition_name} to {self.download_dir}")
            else:
                logging.info(f"Data already exists at {self.zip_file_path}. Skipping download step.")
        except Exception as e:
            logging.error(f"Failed to download competition data: {e}")
            raise

    def extract_data(self, zip_file_path):
        """Extract downloaded data from a zip file."""
        try:
            with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
                zip_ref.extractall(self.download_dir)
            logging.info(f"Extracted zip file {zip_file_path} to {self.download_dir}")
        except Exception as e:
            logging.error(f"Error extracting zip file: {e}")
            raise

class DataProcessing:
    def __init__(self, folder_path):
        self.folder_path = folder_path

    def load_multiple_csv(self):
        """Load multiple CSV files from the folder into a single DataFrame."""
        try:
            csv_files = [f for f in os.listdir(self.folder_path) if f.endswith('.csv')]
            df_list = [next(pd.read_csv(os.path.join(self.folder_path, file), chunksize=1000)) for file in csv_files] #Used chunksize to load the first 1000 rows per file
            combined_df = pd.concat([chunk for chunk in df_list], ignore_index=True)
            logging.info(f"Loaded and concatenated {len(csv_files)} CSV files.")
            return combined_df
        except Exception as e:
            logging.error(f"Failed to load CSV files: {e}")
            raise

    def clean_data(self, df):
        """Clean the data by filling missing values and adjusting data types."""
        try:
            # Fill missing values for numerical columns with the mean
            num_cols = df.select_dtypes(include=['number']).columns
            df[num_cols] = df[num_cols].fillna(df[num_cols].mean())

            # Fill missing values for non-numerical columns with the mode
            non_num_cols = df.select_dtypes(exclude=['number']).columns
            for col in non_num_cols:
                df[col] = df[col].fillna(df[col].mode()[0])

            # Convert datetime to a compatible format
            if 'event_time' in df.columns:
                df['event_time'] = pd.to_datetime(df['event_time'], errors='coerce')  # Convert to datetime and handle errors
                df['event_time'] = df['event_time'].astype('datetime64[ms]')  # Convert to milliseconds precision

            # Convert data types to appropriate formats
            df = df.astype({
                'game_num': 'int32',
                'event_id': 'int32',
                'ball_pos_x': 'float32',
                'ball_pos_y': 'float32',
                'ball_pos_z': 'float32',
                'ball_vel_x': 'float32',
                'ball_vel_y': 'float32',
                'ball_vel_z': 'float32',
                'p0_pos_x': 'float32',
                'p0_pos_y': 'float32',
                'p0_pos_z': 'float32',
                'p0_vel_x': 'float32',
                'p0_vel_y': 'float32',
                'p0_vel_z': 'float32',
                'p0_boost': 'float32',
                'p1_pos_x': 'float32',
                'p1_pos_y': 'float32',
                'p1_pos_z': 'float32',
                'p1_vel_x': 'float32',
                'p1_vel_y': 'float32',
                'p1_vel_z': 'float32',
                'p1_boost': 'float32',
                'p2_pos_x': 'float32',
                'p2_pos_y': 'float32',
                'p2_pos_z': 'float32',
                'p2_vel_x': 'float32',
                'p2_vel_y': 'float32',
                'p2_vel_z': 'float32',
                'p2_boost': 'float32',
                'p3_pos_x': 'float32',
                'p3_pos_y': 'float32',
                'p3_pos_z': 'float32',
                'p3_vel_x': 'float32',
                'p3_vel_y': 'float32',
                'p3_vel_z': 'float32',
                'p3_boost': 'float32',
                'p4_pos_x': 'float32',
                'p4_pos_y': 'float32',
                'p4_pos_z': 'float32',
                'p4_vel_x': 'float32',
                'p4_vel_y': 'float32',
                'p4_vel_z': 'float32',
                'p4_boost': 'float32',
                'p5_pos_x': 'float32',
                'p5_pos_y': 'float32',
                'p5_pos_z': 'float32',
                'p5_vel_x': 'float32',
                'p5_vel_y': 'float32',
                'p5_vel_z': 'float32',
                'p5_boost': 'float32',
                'boost0_timer': 'float32',
                'boost1_timer': 'float32',
                'boost2_timer': 'float32',
                'boost3_timer': 'float32',
                'boost4_timer': 'float32',
                'boost5_timer': 'float32',
                'player_scoring_next': 'int8',
                'team_scoring_next': 'object',
                'team_A_scoring_within_10sec': 'int8',
                'team_B_scoring_within_10sec': 'int8'
            })

            logging.info("Data cleaned successfully with missing values filled and data types adjusted.")
            return df
        except Exception as e:
            logging.error(f"Error during data cleaning: {e}")
            raise


class DataStorage:
    def __init__(self, output_file):
        self.output_file = output_file

    def store_as_parquet(self, data):
        """Store cleaned data as a Parquet file."""
        try:
            table = pa.Table.from_pandas(data)
            pq.write_table(table, self.output_file)
            logging.info(f"Data stored successfully as Parquet at {self.output_file}")
        except Exception as e:
            logging.error(f"Error storing data as Parquet: {e}")
            raise

def log_pipeline_metrics(df, stage):
    """Log the metrics of the pipeline, such as filename, num of columns, num of rows, etc."""
    try:
        metrics = {
            'stage': stage,
            'num_rows': len(df),
            'num_columns': len(df.columns),
            'columns': list(df.columns),
            'info': str(df.info(verbose=True))
        }
        with open('pipeline_metrics.log', 'a') as f:
            f.write(f"Stage: {metrics['stage']}, Rows: {metrics['num_rows']}, Columns: {metrics['num_columns']}\n")
            logging.info(f"Logged pipeline metrics at stage: {stage}")
    except Exception as e:
        logging.error(f"Error logging pipeline metrics: {e}")

def main():
    """Main function to execute the data pipeline."""
    try:
        # Step 1: Data Acquisition
        acquisition = DataAcquisition('tabular-playground-series-oct-2022', './kaggle_data')
        acquisition.authenticate()
        acquisition.download_data()
        acquisition.extract_data('./kaggle_data/tabular-playground-series-oct-2022.zip')


        # Step 2: Data Loading and Processing
        processing = DataProcessing('./kaggle_data')
        df = processing.load_multiple_csv()
        log_pipeline_metrics(df, 'Loaded Data')
        df_cleaned = processing.clean_data(df)
        log_pipeline_metrics(df_cleaned, 'Cleaned Data')

        # Step 3: Data Storage
        storage = DataStorage('rocket_league_data.parquet')
        storage.store_as_parquet(df_cleaned)

        logging.info("Data pipeline executed successfully.")
    except Exception as e:
        logging.error(f"Data pipeline failed: {e}")

if __name__ == "__main__":
    main()
