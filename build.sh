#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

# Download NLTK data
python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords'); nltk.download('punkt_tab')"

# Create the target directory inside the project source
mkdir -p /opt/render/project/src/nltk_data

# Copy the downloaded data to the local directory
cp -r /opt/render/nltk_data/* /opt/render/project/src/nltk_data/
