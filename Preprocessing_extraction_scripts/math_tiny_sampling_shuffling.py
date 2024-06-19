import os
import pandas as pd
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def save_data_to_file(data, output_file):
    data.to_csv(output_file, index=False)
    logging.info(f"Data saved to: {output_file}")

data_dir = 'D://MLMATH'
output_dir = 'D://MLMATH'
train_file = os.path.join(output_dir, 'final_tiny.csv')
test_file = os.path.join(output_dir, 'final_tiny_test.csv')

# Initialize lists to store sampled data
train_data = []
test_data = []

# Process each CSV file in the directory
for file in os.listdir(data_dir):
    if file.endswith('.csv'):
        file_path = os.path.join(data_dir, file)
        logging.info(f"Processing file: {file_path}")
        df_temp = pd.read_csv(file_path)
        logging.info(f"Loaded {len(df_temp)} rows from {file}")

        # Sample 10 rows for training and another 10 for testing
        train_sample = df_temp.sample(min(10, len(df_temp)), random_state=42)
        remaining_data = df_temp.drop(train_sample.index)
        test_sample = remaining_data.sample(min(10, len(remaining_data)), random_state=42)

        # Append samples to the respective lists
        train_data.append(train_sample)
        test_data.append(test_sample)

# Combine all sampled data
train_df = pd.concat(train_data, ignore_index=True)
test_df = pd.concat(test_data, ignore_index=True)

# Shuffle the final dataframes
train_df = train_df.sample(frac=1, random_state=42).reset_index(drop=True)
test_df = test_df.sample(frac=1, random_state=42).reset_index(drop=True)

# Perform any preprocessing or normalization here if needed

# Save the final data to CSV files
save_data_to_file(train_df, train_file)
save_data_to_file(test_df, test_file)

logging.info("Dataset combined, shuffled, preprocessed, and saved successfully for both training and testing.")
