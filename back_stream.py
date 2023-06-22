import pandas as pd
import numpy as np
import ance_sim
from sentence_transformers import SentenceTransformer

def similarity(input):
    load_embeddings = np.load('/userHome/userhome4/kyumin/ANCE/title_embeddings.npy')
    transpose_embedding = np.transpose(load_embeddings)
    
    res = ance_sim.cos_similarity(input, transpose_embedding)
    return res
def predict(input):

    model = SentenceTransformer('sentence-transformers/msmarco-roberta-base-ance-firstp')
    input_embedding = model.encode(input)

    sim_res = similarity(input_embedding)
    idx = np.where(sim_res == np.max(sim_res))[0][0]
    load_title = pd.read_csv('/userHome/userhome4/kyumin/ANCE/MINDsmall_dev/news_title.csv')
    print(load_title.loc[idx].Title)
    return None