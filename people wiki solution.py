# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
dataset = pd.read_csv('people_wiki (1).csv')
import re
patterns = ['Elton John']
for i in range (0, 59071):
    for pattern in patterns:
        if re.search(pattern, dataset['name'][i]):
            Elton_John = dataset.ix[i]
corpus = []
for i in range (0, 59071):
    wiki = re.sub('[^a-zA-Z]', ' ', dataset['text'][i])
    wiki = wiki.lower()
    corpus.append(wiki)

from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer()
counts = cv.fit_transform(corpus).toarray()
from sklearn.feature_extraction.text import TfidfTransformer
transformer = TfidfTransformer(smooth_idf=False)
X = transformer.fit_transform(counts).toarray()

corpus_1 = []
wiki_1 = re.sub('[^a-zA-Z]', ' ', dataset['text'][19923])
wiki_1 = wiki_1.lower()
corpus_1.append(wiki_1)
cv_1 = CountVectorizer()
counts_1 = cv_1.fit_transform(corpus_1).toarray()
X_1 = transformer.transform(counts_1).toarray()
cv_1.vocabulary_




  
   