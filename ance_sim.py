from sentence_transformers import SentenceTransformer


import numpy as np

def cos_similarity(v1, v2):
    dot_product = np.dot(v1, v2)
    l2_norm = (np.sqrt(sum(np.square(v1))) * np.sqrt(sum(np.square(v2))))
    similarity = dot_product / l2_norm     
    
    return similarity

sentences = []



model = SentenceTransformer('sentence-transformers/msmarco-roberta-base-ance-firstp')
def sim(sen1, sen2):
    sentences.append(sen1)
    sentences.append(sen2)
    embeddings = model.encode(sentences)
    cosine_similar = cos_similarity(embeddings[0],embeddings[1])
    return cosine_similar

