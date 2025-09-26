# SentimentPro: Sentiment Analysis Web App

SentimentPro is a modern Flask web application for analyzing the sentiment of user reviews. Upload text or Excel/CSV files, and visualize sentiment breakdowns with beautiful interactive charts.

## Features
- **Instant Sentiment Prediction:** Enter a review and get real-time sentiment analysis (Good, Bad, Neutral).
- **Bulk Analysis via Excel/CSV Upload:** Upload files and see a breakdown of review sentiments.
- **Interactive Charts:** Visualize sentiment distribution with clear, modern charts.
- **Clean, Responsive UI:** Built with Bootstrap and custom styles for a seamless experience.

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
