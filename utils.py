import numpy as np
from nltk.cluster.util import cosine_distance
from nltk.corpus import stopwords

def get_similarity_between_sentences(sent1, sent2, stopwords):
    vocab_size = len(set(sent1 + sent2))
    all_words = list(set(sent1 + sent2))
    sent1_vec = np.zeros((vocab_size,))
    sent2_vec = np.zeros((vocab_size,))

    for word in sent1:
        if word not in stopwords:
            sent1_vec[all_words.index(word)] += 1

    for word in sent2:
        if word not in stopwords:
            sent2_vec[all_words.index(word)] += 1
    
    return cosine_distance(sent1_vec, sent2_vec)

def get_similarity_between_sentences(sent1, sent2, stopwords):
    vocab_size = len(set(sent1 + sent2))
    all_words = list(set(sent1 + sent2))
    sent1_vec = np.zeros((vocab_size,))
    sent2_vec = np.zeros((vocab_size,))

    for word in sent1:
        if word not in stopwords:
            sent1_vec[all_words.index(word)] += 1

    for word in sent2:
        if word not in stopwords:
            sent2_vec[all_words.index(word)] += 1
    
    return cosine_distance(sent1_vec, sent2_vec)

