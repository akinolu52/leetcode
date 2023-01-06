import networkx as nx
import nltk
import numpy as np
from nltk.cluster.util import cosine_distance
from nltk.corpus import stopwords

nltk.download('cosine_distance')
# nltk.download('stopwords')
# nltk.download('corpus')

def summarize(text, num_sentences):
    # Tokenize the text and retrieve the list of sentences
    sentences = nltk.sent_tokenize(text)

    # If the number of sentences is less than or equal to the desired number of sentences, return the original text
    if len(sentences) <= num_sentences:
        return text

    # Calculate the similarity distance between each pair of sentences
    similarity_matrix = np.zeros((len(sentences), len(sentences)))
    for i in range(len(sentences)):
        for j in range(len(sentences)):
            if i != j:
                similarity_matrix[i][j] = cosine_distance(sentences[i], sentences[j])

    # Build the graph using the similarity matrix
    sentences_graph = nx.from_numpy_array(similarity_matrix)

    # Use PageRank to score the sentences
    scores = nx.pagerank(sentences_graph)

    # Sort the sentences by their PageRank scores
    ranked_sentences = sorted(
        ((scores[i], s) for i, s in enumerate(sentences)), reverse=True)

    # Return the top ranked num_sentences sentences as the summary
    summary = []
    for i in range(num_sentences):
        summary.append(ranked_sentences[i][1])
    return " ".join(summary)


# Test the summarize function
text = "This is a sample text. It has multiple sentences. The text summarization function should summarize this text by selecting the most important sentences. Let's see how it works."
num_sentences = 2
summary = summarize(text, num_sentences)
print(summary)
