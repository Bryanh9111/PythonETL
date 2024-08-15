import pandas as pd
import os
from config.file_config import FILE_PATH

def get_combined_headers(files):
    combined_columns = set()
    for file_name in files:
        file_path = os.path.join(FILE_PATH, file_name)
        df = pd.read_csv(file_path)
        combined_columns.update(df.columns)
    return list(combined_columns)

def read_data_with_combined_headers(file_name, combined_headers):
    file_path = os.path.join(FILE_PATH, file_name)
    df = pd.read_csv(file_path)
    
    # Ensure all columns in combined_headers are present in the DataFrame
    for column in combined_headers:
        if column not in df.columns:
            df[column] = None
    
    # Reorder the columns to match the combined headers
    df = df[combined_headers]
    
    return df
