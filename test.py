import pickle
from gensim.models.keyedvectors import KeyedVectors
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import json
import subprocess
import time
import sys

modelname = 'glove_model.pickle'
infile = open(modelname,'rb')
glove_model = pickle.load(infile)
infile.close()

print(glove_model.similarity('architecture','resource'))

