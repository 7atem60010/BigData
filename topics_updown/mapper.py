#!/usr/bin/python3
import sys
import json
import string
from collections import Counter


#translator = string.maketrans("  ", string.punctuation)
stop_words = {'hadn', 'having', "wouldn't", 've', "she's", 'she', "wasn't", "doesn't", 'has', 'off', 'he', 'which', 'other', 'if', 'd', 'her', 'are', 'these', 'so', 'own', "hadn't", 'up', 'had', 'ma', 'shouldn', "won't", 'haven', 'and', 'here', 'each', 'from', 'a', "shan't", "couldn't", "should've", 'him', 'into', "you'll", 'o', 'ourselves', 'on', 'of', 'being', 'y', "aren't", 'doing', 'don', 'couldn', 'm', 'what', 'than', "haven't", 'our', 'through', 'same', 'you', 'their', 'those', 'its', 'yourself', 'ours', 'who', 'nor', 'do', 'again', 'deleted', 'them', 'more', 'yourselves', "you've", 'in', 'did', 'how', 'not', 'until', 'his', "don't", 'when', 'against', 'does', 'himself', 'during', 'some', 'such', 'aren', 'be', 'themselves', 'because', 'should', "that'll", 'both', 'down', "mustn't", 'we', "it's", 'under', 'once', 'been', 'then', 'will', 'me', 'mustn', 'i', "mightn't", 'itself', 'about', 'most', 'ain', 't', 'why', 'only', 'weren', "you'd", 'where', 're', 'too', 'but', 'all', 'between', 'wouldn', 'while', 'have', 'didn', 'they', 'for', 'or', 'out', 'the', 'few', 'hasn', 'was', "you're", 'am', "shouldn't", 'just', 'isn', 'there', 'mightn', 'very', 'won', 'above', 'with', 'is', 'hers', 'wasn', 'now', 'll', 'that', 'over', 's', 'after', "hasn't", 'yours', 'any', 'my', "needn't", 'at', 'before', 'no', "didn't", 'shan', "weren't", 'can', 'it', 'were', 'your', 'whom', "isn't", 'below', 'as', 'further', 'needn', 'herself', 'doesn', 'by', 'an', 'this', 'to', 'myself', 'theirs'}


for line in sys.stdin:
    y = json.loads(line)
    word_tokens = y['body'].lower().split()
    filtered_sentence = [w for w in word_tokens if not w in stop_words]
    topic = None
    if len(filtered_sentence) ==  0:
        topic = None
    else:
        occurence_count = Counter(filtered_sentence)
        if occurence_count.most_common(1)[0][1] > 1 :
            topic=occurence_count.most_common(1)[0][0]
            if y['ups']>0:
                print(topic , y['ups'])
