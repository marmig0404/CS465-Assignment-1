"""
# CS465-W22-IRproject-Group4-BackEnd.py
#
# CS465/665, W22, and Project #4
# Martin Miglio and Johnathan Max Tomlin
#
# This file will handle the backend processing of this information retrieval program
"""

import os


def load_files(directory_name):
    """
    # load in file names
    """

    file_list = []
    for root, dirs, files in os.walk('documents/'):
        for file in files:
            if(file.endswith(".txt")):
                file_list.append(os.path.join(root, file))
    return file_list


def read_contents(file_list):
    """
    # read file contents
    """

    file_contents = []
    lines = ''
    file_num = 0
    position = 0
    for file in file_list:
        position = 0
        lines = open(file, 'r', errors='ignore').readlines()
        for line in lines:
            for word in line.split(' '):
                file_contents.append([word, file_num, position])
                position = position + 1
        file_num = file_num + 1
    return file_contents


def add_contents_to_dictionary(file_contents):
    """
    # move contents to dictionary
    """

    index = dict()
    for word in file_contents:
        if word[0] not in index:
            index.update({word[0]: {word[1]: [word[2]]}})
        else:
            if word[1] not in index.get(word[0]):
                index[word[0]].update({word[1]: word[2:]})
            else:
                index[word[0]][word[1]].append(word[2])
    index = dict(sorted(index.items()))
    return index

