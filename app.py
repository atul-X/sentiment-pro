from flask import Flask,render_template,url_for,request, jsonify
import pandas as pd
import numpy as np
import pickle
import string
from nltk import word_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
from Az import text_process
app = Flask(__name__)


@app.route('/')
def home():
	return render_template('home.html')
@app.route("/upload", methods=['GET', 'POST'])


@app.route('/predict',methods=['POST'])
def predict():

    pdict=open("Model.pickle","rb")
    cl = pickle.load(pdict)
    
    pickle_in = open("cv1","rb")
    clf = pickle.load(pickle_in)

   
    if request.method == 'POST':
	    message = request.form['message']
	    data = [message]
	    vect = clf.transform(data)
	    my_prediction = cl.predict(vect)
    return render_template('result.html',prediction = my_prediction)
colors = [
    "#F7464A", "#46BFBD", "#FDB45C"]

@app.route('/charts', methods=['GET', 'POST'])
def charts():
    pdict=open("Model.pickle","rb")
    cl = pickle.load(pdict)
    pickle_in = open("cv1","rb")
    clf = pickle.load(pickle_in)
    if request.method == 'POST' and 'file' in request.files:
        filename = pd.read_csv(request.files.get('file'))
        Data=filename['review']
        vect = clf.transform(Data)
        my_prediction = cl.predict(vect)
        a=my_prediction.tolist().count('good')
        b=my_prediction.tolist().count('bad')
        c=my_prediction.tolist().count('neutral')
        bar_labels='Good','Bad','Netural'
        bar_values=[a,b,c]
        return render_template('pie_chart.html', title='reviews charts', max=100, labels=bar_labels, values=bar_values)
    return render_template('pie_chart.html')

if __name__ == '__main__':
    app.run()
