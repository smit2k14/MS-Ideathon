import nltk
import sys
import networkx as nx
from utils import *
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("See the usage on how to use this")
        exit()

    try:
        stop_words = stopwords.words('english')
    except:
        nltk.download('stopwords')
        stop_words = stopwords.words('english')
    
    with open(sys.argv[1]) as f:
        dataset = f.read()

    dataset = dataset.split('.')

    similarity_matrix = get_similarity_matrix(dataset, stop_words)
    sentence_similarity_graph = nx.from_numpy_array(similarity_matrix)
    scores = nx.pagerank(sentence_similarity_graph)

    ranked_sentence = sorted(((scores[i],s) for i,s in enumerate(dataset)))
    
    summarized_data = []
    n_summ_sent = sys.argv[2]
    for i in range(5):
        summarized_data.append("".join(ranked_sentence[i][1]))

    summarized_data = ".".join(summarized_data)
    with open('summarized_data.txt', 'w') as f:
        f.write(summarized_data)
