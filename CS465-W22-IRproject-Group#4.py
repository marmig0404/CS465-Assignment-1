#Johnathan Max Tomlin & Martin Miglio
#CS 465/665, W22, Project # 1

import numpy as np
import pandas as pd
import os

#Create the inverted index (the dictionary and postings lists) for your
#  collection of documents
# load in file names
filelist = []
for root, dirs, files in os.walk('documents/'):
    for file in files:
        if(file.endswith(".txt")):
            filelist.append(os.path.join(root,file))
# load in file contents
filecontents = []
lines = ''
filenum = -1
position = 0
for file in filelist:
    filenum = filenum + 1
    position = 0
    lines = open(file, 'r', errors = 'ignore').readlines()
    for line in lines:
        for word in line.split(' '):
            filecontents.append([word, filenum, position])
            position = position + 1
#  Perform simple tokenization and normalization of the text such as removing
#    digits, punctuation marks, etc.
#   TODO: TOKENIZATION/NORMALIZATION/ETC. GOES HERE
# move contents to dictionary
index = dict()
for word in filecontents:
    if word[0] not in index:
        index.update({word[0]: {word[1]: [word[2]]}})
    else:
        if word[1] not in index.get(word[0]):
            index[word[0]].update({word[1]: word[2:]})
        else:
            index[word[0]][word[1]].append(word[2])
index = dict(sorted(index.items()))
#print(index) #uncomment to view raw dictionary (warning: large)
#TODO: EVERYTHING FOR AFTER THE INDEX IS CREATED
# (Parse and execute simple queries) && (Statistics:)