from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity, linear_kernel

import numpy as np

def cos_similarity(v1, v2):
    dot_product = np.dot(v1, v2)
    l2_norm = (np.sqrt(sum(np.square(v1))) * np.sqrt(sum(np.square(v2))))
    similarity = dot_product / l2_norm     
    
    return similarity

#sentences = ["Moscow buildings damaged in drone attack", "malaysia investiating possible looting of word war II British ship"]

#model = SentenceTransformer('sentence-transformers/msmarco-roberta-base-ance-firstp')
#embeddings = model.encode(sentences)
#cosine_similar = cos_similarity(embeddings[0],embeddings[1])

#print(cosine_similar)

load_file = np.load('/userHome/userhome4/kyumin/ANCE/title_embeddings.npy')
print(load_file[0:2])
