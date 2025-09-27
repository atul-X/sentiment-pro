#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

# Download NLTK data
python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords'); nltk.download('punkt_tab')"

# Copy the downloaded data to a local directory in the project
cp -r /opt/render/nltk_data/* /opt/render/project/src/nltk_data/
