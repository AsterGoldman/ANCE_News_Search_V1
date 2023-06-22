import pandas as pd
import numpy as np
import pickle
from sentence_transformers import SentenceTransformer

df = pd.read_csv('/userHome/userhome4/kyumin/ANCE/MINDsmall_dev/news_output.csv', usecols=['Number', 'Title'])

title_list = df['Title'].values.tolist()
model = SentenceTransformer('sentence-transformers/msmarco-roberta-base-ance-firstp')
embeddings = model.encode(title_list)
np.save('/userHome/userhome4/kyumin/ANCE/title_embeddings', embeddings)
#embeddings = embeddings.tolist()

#with open('/userHome/userhome4/kyumin/ANCE.pkl',' wb') as file:
#    pickle.dump(embeddings, file, protocol=3)