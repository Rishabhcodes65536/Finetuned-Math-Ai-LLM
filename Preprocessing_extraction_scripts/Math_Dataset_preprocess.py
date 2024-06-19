import os
import pandas as pd
from datasets import Dataset, DatasetDict
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def load_data_from_folder(data_dir):
    logging.info(f"Entering directory: {data_dir}")
    all_data = []
    for file in os.listdir(data_dir):
        if file.endswith('.csv'):
            file_path = os.path.join(data_dir, file)
            logging.info(f"Processing file: {file_path}")
            df = pd.read_csv(file_path)
            logging.info(f"Loaded {len(df)} rows from {file}")
            all_data.append(df)
    logging.info("All files loaded successfully.")
    return pd.concat(all_data, ignore_index=True)

data_dir = 'D://MLMATH'
df = load_data_from_folder(data_dir)
logging.info(f"Total rows in the combined dataset: {len(df)}")
df = df[['question', 'answer']]  # Ensure only relevant columns are kept
df.dropna(inplace=True)  # Remove rows with missing values
df.reset_index(drop=True, inplace=True)
logging.info("Dataset cleaned and preprocessed successfully.")
