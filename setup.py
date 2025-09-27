import nltk
import os

# Define the download directory, which corresponds to the nltk.cfg file
download_dir = './nltk_data'

# Create the directory if it doesn't exist
if not os.path.exists(download_dir):
    os.makedirs(download_dir)

# List of packages to download
packages = ['punkt', 'stopwords', 'wordnet', 'omw-1.4', 'punkt_tab']

# Download necessary NLTK data packages to the specified directory
for package in packages:
    try:
        nltk.data.find(f'tokenizers/{package}')
    except LookupError:
        nltk.download(package, download_dir=download_dir)

print(f"NLTK data packages downloaded successfully to {download_dir}.")

