import os
from kaggle.api.kaggle_api_extended import KaggleApi

# Create 'data' folder if it doesn't exist
os.makedirs('data', exist_ok=True)

# Initialize Kaggle API
api = KaggleApi()
api.authenticate()

# Dataset reference (replace with your actual dataset slug)
dataset = 'rmisra/news-category-dataset'  # example, replace with the real dataset if needed
file_name = 'ds_salaries.csv'             # the CSV you want

# Download the dataset
print("Downloading dataset...")
api.dataset_download_file(dataset, file_name, path='data', unzip=True)
print(f"Dataset downloaded and saved to data/{file_name}")
