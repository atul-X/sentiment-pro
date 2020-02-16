# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 23:00:30 2020

@author: Atul
"""
import nltk
nltk.download('punkt')
nltk.download('stopwords')
import string
from nltk import word_tokenize
from nltk.corpus import stopwords

def text_process(text):
    tokenized_sent = [word.lower() for word in word_tokenize(text)]
    rare_words = ['``', "''", '...', '..', '039', '1.5', 'ive']
    useless_words = stopwords.words("english") + list(string.punctuation) + rare_words
    return [word for word in tokenized_sent if not word in useless_words]
