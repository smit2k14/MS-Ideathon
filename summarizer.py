import nltk
import networkx as nx
from utils import *

if __name__ == '__main__':
    try:
        stop_words = stopwords.words('english')
    except:
        nltk.download('stopwords')
        stop_words = stopwords.words('english')
    
    with open('rasputin_data.txt') as f:
        dataset = f.read()

    dataset = dataset.split('.')

    similarity_matrix = get_similarity_matrix(dataset, stop_words)
    sentence_similarity_graph = nx.from_numpy_array(similarity_matrix)
    scores = nx.pagerank(sentence_similarity_graph)

    ranked_sentence = sorted(((scores[i],s) for i,s in enumerate(dataset)))
    
    summarized_data = []
    for i in range(5):
        summarized_data.append("".join(ranked_sentence[i][1]))

    summarized_data = ".".join(summarized_data)
    with open('summarized_data.txt', 'w') as f:
        f.write(summarized_data)