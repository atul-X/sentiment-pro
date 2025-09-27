# SentimentPro: Sentiment Analysis Web App

SentimentPro is a modern Flask web application for analyzing the sentiment of user reviews. Upload text or Excel/CSV files, and visualize sentiment breakdowns with beautiful interactive charts.

## Features
- **Instant Sentiment Prediction:** Enter a review and get real-time sentiment analysis (Good, Bad, Neutral).
- **Bulk Analysis via Excel/CSV Upload:** Upload files and see a breakdown of review sentiments.
- **Interactive Charts:** Visualize sentiment distribution with clear, modern charts.
- **Clean, Responsive UI:** Built with Bootstrap and custom styles for a seamless experience.

## Architecture

SentimentPro is a modular Flask web app with a clear separation between the web interface, preprocessing, and machine learning model. It uses NLTK for text processing and scikit-learn for sentiment prediction.

## About the Model & Training Data

- **Model Type:** Multinomial Naive Bayes classifier (scikit-learn)
- **Training Data:** Drugs.com Drug Review Dataset (from [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Drug+Review+Dataset+%28Drugs.com%29)), combining both train and test splits.
- **Data Size:** ~215,000+ user reviews of medications.
- **Labeling:**
    - Reviews are labeled as:
        - `positive` if the rating is 8 or above
        - `negative` if the rating is 4 or below
        - `neutral` otherwise
- **Text Processing:**
    - Reviews are cleaned, tokenized, lowercased, and filtered for stopwords/punctuation using NLTK.
    - Features are extracted using CountVectorizer.
- **Prediction:**
    - The model predicts whether a review is positive, negative, or neutral based on the text content.

### Why Drugs.com Data?
- It is a real-world, large-scale dataset of user experiences with medications, making it ideal for demonstrating general sentiment analysis workflows.

### Note
- The model is generic and can be retrained on your own labeled review data for other domains (e.g., product reviews, movie reviews, etc.)

### High-Level Architecture
```mermaid
flowchart TD
    User[User (Web Browser)] -->|HTTP| Flask[Flask Web App]
    Flask -->|Text Input| Preprocess[Text Preprocessing (NLTK)]
    Preprocess -->|Features| Model[Trained ML Model (scikit-learn)]
    Model -->|Prediction| Flask
    Flask -->|HTML Response| User
    Flask -->|Excel Upload| Pandas[Pandas Data Processing]
    Pandas --> Preprocess
```

### Review Prediction Flow
```mermaid
flowchart LR
    A[User submits review] --> B[Text cleaned & tokenized (NLTK)]
    B --> C[Stopwords & rare words removed]
    C --> D[Vectorized (CountVectorizer)]
    D --> E[Prediction (MultinomialNB)]
    E --> F[Result shown in UI]
```

## Getting Started

### Prerequisites
- Python 3.8+
- pip
- (Recommended) Create and activate a virtual environment

### Installation
```bash
pip install -r requirements.txt
```

### Running Locally
```bash
# Activate your virtual environment if needed
export FLASK_APP=app.py
flask run
```
Visit [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

### Production Deployment
- Use a WSGI server like Gunicorn (see `Procfile` for Heroku/Render)
- Ensure `Model.pickle` and `cv1` are present in the root directory

## Folder Structure
```
├── app.py                # Main Flask application
├── text_utils.py          # Text processing utilities
├── requirements.txt      # Python dependencies
├── Procfile              # For deployment (Heroku/Render)
├── Model.pickle          # Trained ML model (required for prod)
├── cv1                   # Trained vectorizer (required for prod)
├── static/
│   ├── icon.png          # App icon
│   ├── style.css         # Custom styles
│   └── ...               # Other images/assets
├── templates/
│   ├── home.html         # Main page
│   ├── pie_chart.html    # Excel chart page
│   ├── result.html       # Prediction result page
│   └── about.html        # About page
```

## Credits
- Developed by Atul Kumar and contributors.
- Built with Flask, scikit-learn, pandas, Chart.js, Bootstrap.

---
For questions or contributions, open an issue or pull request.
