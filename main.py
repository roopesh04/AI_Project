import pickle
from gensim.models.keyedvectors import KeyedVectors
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import json
import subprocess
import time
import sys

start = time.time()

class video_search:

    def load_model(self):
        modelname = 'glove_model.pickle'
        infile = open(modelname,'rb')
        glove_model = pickle.load(infile)
        infile.close()
        return glove_model

    def pass_json_for_getting_list(self, filepath='data.json'):
        with open(filepath) as transcribe:
            dat=json.load(transcribe)
        all_words = []
        n=(len(dat['results']['items']))
        a=dat['results']['items']
        for i in range(0,n):
            b=[]
            b.append(a[i]["alternatives"][0]["content"])
            try:
                b.append(float(a[i]["start_time"]))
                b.append(float(a[i]["end_time"]))
                all_words.append(b)
            except:
                continue

        return all_words
        
    def filtering_list(self, all_words):
        filtered_list = []
        for word in all_words:
            example_sent = word[0]
            stop_words = set(stopwords.words('english')) 
            word_tokens = word_tokenize(example_sent) 
            for w in word_tokens: 
                if w not in stop_words: 
                    filtered_list.append([w,word[1],word[2]])
        return filtered_list
        
    def algorithm (self, filtered_list, input_word, model):
        modelname = 'glove_model.pickle'
        infile = open(modelname,'rb')
        glove_model = pickle.load(infile)
        infile.close()
        print(input_word)
        pos,counter = [],[]
        distance, count = 0, 0
        for element in filtered_list:
            word = element[0] 
            if word == input_word:
                pos.append(count)
            count = count + 1
        print("Pos",pos)
        print("Length",len(pos))
        for i in range (0,len(pos)-1):
            for j in range (pos[i]+1,pos[i+1]):
                try:
                    distance = distance + glove_model.similarity(input_word,filtered_list[j][0])
                    #print(distance)
                    #print("1")
                    #print("distance",distance)
                except:
                    # e = sys.exc_info()[0]
                    # print("<p>Error: %s</p>" % e)
                    #print("2")
                    pass
            counter.append(distance/j)
            print("distance",distance)
            distance = 0
            maximum_value = max(counter)
            # print("maximum value",maximum_value)
            # print(counter)
            # print("Output Value",filtered_list[pos[counter.index(maximum_value)]][1])
        print("Output value",filtered_list[pos[counter.index(maximum_value)]][1])
        return (filtered_list[pos[counter.index(maximum_value)]][1])

test = video_search()



        
