import os
import pandas as pd
import logging
import random

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def save_data_to_file(data, output_dir):
    output_file = os.path.join(output_dir, 'final_small.csv')
    data.to_csv(output_file, index=False)
    logging.info(f"Final data saved to: {output_file}")

data_dir = 'D://MLMATH'
output_dir = 'D://MLMATH'


# Extract up to 10,000 rows from each file
sampled_data = []
for file in os.listdir(data_dir):
    if file.endswith('.csv'):
        file_path = os.path.join(data_dir, file)
        logging.info(f"Processing file: {file_path}")
        df_temp = pd.read_csv(file_path)
        logging.info(f"Loaded {len(df_temp)} rows from {file}")
        sampled_data.append(df_temp.sample(min(10, len(df_temp)), random_state=42))

# Combine all sampled data
final_df = pd.concat(sampled_data, ignore_index=True)

# Shuffle the final dataframe
final_df = final_df.sample(frac=1, random_state=42).reset_index(drop=True)


# Save the final data to a CSV file
save_data_to_file(final_df, output_dir)

logging.info("Dataset combined, shuffled, preprocessed, and saved successfully.")
