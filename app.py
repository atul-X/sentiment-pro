import nltk
import os

# Define the path to the local nltk_data directory and add it to NLTK's path.
# This ensures that data copied during the build is found by the running application.
project_root = os.path.dirname(os.path.abspath(__file__))
nltk_data_path = os.path.join(project_root, 'nltk_data')
if nltk_data_path not in nltk.data.path:
    nltk.data.path.append(nltk_data_path)

from flask import Flask,render_template,url_for,request, jsonify, redirect
import pandas as pd
import numpy as np
import pickle
import string
from nltk import word_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
from text_utils import text_process
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route("/upload", methods=['GET', 'POST'])



@app.route('/predict',methods=['POST'])
def predict():
    pdict = open("Model.pickle", "rb")
    cl = pickle.load(pdict)
    pickle_in = open("cv1", "rb")
    clf = pickle.load(pickle_in)
    current_year = datetime.now().year
    if request.method == 'POST':
        message = request.form['message']
        data = [message]
        vect = clf.transform(data)
        my_prediction = cl.predict(vect)
        # Ensure prediction is a string, not a list
        prediction_str = my_prediction[0] if hasattr(my_prediction, '__getitem__') else my_prediction
        return render_template('result.html', prediction=prediction_str, current_year=current_year)
    return render_template('result.html', prediction=None, current_year=current_year)

colors = [
    "#F7464A", "#46BFBD", "#FDB45C"]

@app.route('/charts', methods=['GET', 'POST'])
def charts():
    # Only load model if POST with file, else just render chart page
    if request.method == 'POST' and 'file' in request.files:
        try:
            pdict = open("Model.pickle", "rb")
            cl = pickle.load(pdict)
            pickle_in = open("cv1", "rb")
            clf = pickle.load(pickle_in)
            file = request.files.get('file')
            if file and file.filename.endswith(('.csv', '.xlsx')):
                if file.filename.endswith('.csv'):
                    df = pd.read_csv(file)
                else:
                    df = pd.read_excel(file)
                if 'review' not in df.columns:
                    return render_template('pie_chart.html', title='reviews charts', max=100, labels=[], values=[], error='Excel/CSV must have a "review" column.', year=datetime.now().year)
                Data = df['review']
                vect = clf.transform(Data)
                my_prediction = cl.predict(vect)
                a = my_prediction.tolist().count('good')
                b = my_prediction.tolist().count('bad')
                c = my_prediction.tolist().count('neutral')
                bar_labels = ['Good', 'Bad', 'Neutral']
                bar_values = [a, b, c]
                max_count = max(bar_values) if bar_values else 100
                return render_template('pie_chart.html', title='Reviews Chart', max=max_count, labels=bar_labels, values=bar_values, year=datetime.now().year)
            else:
                return render_template('pie_chart.html', title='reviews charts', max=100, labels=[], values=[], error='Please upload a CSV or Excel file.', year=datetime.now().year)
        except Exception as e:
            return render_template('pie_chart.html', title='reviews charts', max=100, labels=[], values=[], error=f'Error: {e}', year=datetime.now().year)
    # GET or no file
    return render_template('pie_chart.html', title='Reviews Chart', max=100, labels=[], values=[], year=datetime.now().year)

if __name__ == '__main__':
    app.run()
