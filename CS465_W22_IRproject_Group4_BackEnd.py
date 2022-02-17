"""
# CS465-W22-IRproject-Group4-BackEnd.py
#
# CS465/665, W22, and Project #1
# Martin Miglio and Johnathan Max Tomlin
#
# This file will handle the backend processing of this information retrieval program
"""

import os
import re


def load_files(directory_name):
    """
    # load in file names
    # -jmt
    """
    file_list = []
    file_num = 0
    for root, _, files in os.walk(directory_name):
        for file in files:
            if file.endswith(".txt"):
                file_list.append([os.path.join(root, file), file_num])
                file_num = file_num + 1
    return file_list


def read_contents(file_list):
    """
    # read file contents
    # -jmt
    """
    file_contents = []
    lines = ''
    position = 0
    for file in file_list:
        position = 0
        with open(file[0], 'r', errors='ignore', encoding="utf-8") as openfile:
            lines = openfile.readlines()
        for line in lines:
            for word in line.split(' '):
                word = tokenize_normalize(word)
                if word != '':
                    file_contents.append([word, file[1], position])
                position = position + 1
    return file_contents


def tokenize_normalize(word):
    """
    # simple tokenization and normalization
    # -jmt
    """
    normalized_token = word.lower()
    normalized_token = re.sub(r'\d+', '', normalized_token)
    normalized_token = re.sub(r'[^\w\s]', '', normalized_token)
    normalized_token = normalized_token.strip()
    return normalized_token


def add_contents_to_dictionary(file_contents):
    """
    # move contents to dictionary
    # -jmt
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


def distinct_terms(index):
    """
    # returns the number of distinct terms in all documents
    # -jmt
    """
    terms = 0
    for _ in index:
        terms = terms + 1
    return terms


def distinct_terms_doc(index, docnum):
    """
    # returns the number of distinct terms in a specified document
    # -jmt
    """
    terms = 0
    for term in index.values():
        if docnum in term:
            terms = terms + 1
    return terms


def total_words(index):
    """
    # returns the total number of words in all documents
    # -jmt
    """
    words = 0
    for term in index.values():
        for doc in term.values():
            for _ in doc:
                words = words + 1
    return words


def total_words_doc(index, docnum):
    """
    # returns the total number of words in a specified document
    # -jmt
    """
    words = 0
    for term in index.values():
        if docnum in term:
            for _ in term[docnum]:
                words = words + 1
    return words


def term_frequency(index, term):
    """
    # returns the total number of times a term is used
    # -jmt
    """
    freq = 0
    if term in index:
        for doc in index[term].values():
            for _ in doc:
                freq = freq + 1
    return freq


def all_term_frequencies(index):
    """
    # returns all term frequencies
    # -jmt
    """
    tf_index = []
    for term in index:
        tf_index.append([term, term_frequency(index, term)])
    return sorted(tf_index, key=lambda x: x[1], reverse=True)


def posting_list_term(index, term):
    """
    # returns the documents which contain a term
    # -jmt
    """
    posting = []
    if term in index:
        posting = list(index[term].keys())
    return posting


def specified_word_frequencies(index, frequency_rank):
    """
    # returns a term at a specified rank of frequency
    # -jmt & mm
    """
    term_frequencies = all_term_frequencies(index)
    if len(term_frequencies) <= frequency_rank:
        return ["n/a", "n/a"]
    return term_frequencies[frequency_rank]


def initialize(directory_name):
    """
    # read files and make index
    # -mm
    """
    file_list = load_files(directory_name)
    file_contents = read_contents(file_list)
    return add_contents_to_dictionary(file_contents)
