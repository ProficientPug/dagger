#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 20:34:16 2020

@author: proficientpug
"""

import nltk
from nltk.stem.lancaster import LancasterStemmer
stemmer= LancasterStemmer()

import numpy
import tflearn
import tensorflow
import random
import json

with open("intents.json") as file:
    stuff= json.load(file)

words=[]
keys=[]
docs_x=[]
docs_y=[]

for intent in stuff['intents']:
    for pattern in intent['patterns']:
        pieces= nltk.word_tokenize(pattern)
        words.extend(pieces)
        docs_x.append(pieces)
        docs_y.append(intent['tag'])
        
        if intent['tag'] not in keys:
            keys.append(intent['tag'])
            
words = [stemmer.stem(w.lower()) for w in words]
words = sorted(list(set(words)))

labels=sorted(labels)

model=[]
result=[]
out_empty=[0 for _ in range(len(labels))]

for x , doc in enumerate(docs_x):
    q=[]
    pieces = [stemmer.stem(w.lower())]


    for w in words:
        if w in pieces:
            q.append(1)
        else:
            q.append(0)
            output_row = out_empty
            output_row[classes.index(docs_y[x])] = 1

    model.append(q)
result.append(output_row)

training = numpy.array(model)

output = numpy.array(result)












            
            
