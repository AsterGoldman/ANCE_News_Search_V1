import pandas as pd
from sentence_transformers import SentenceTransformer

#df = pd.read_csv('/userHome/userhome4/kyumin/ANCE/MINDsmall_dev/news.tsv', sep='\t')
#df.to_csv('/userHome/userhome4/kyumin/ANCE/MINDsmall_dev/news_output.csv', index = False)
df = pd.read_csv('/userHome/userhome4/kyumin/ANCE/MINDsmall_dev/news_output.csv', usecols=['Number', 'Title'])
#df = pd.read_csv('/userHome/userhome4/kyumin/ANCE/MINDsmall_dev/movie-ratings.csv')
#df.columns =["Number", "Category", "Sub_category", "Title", "Content", "Hyper-link","Desc","Others"]
df.to_csv('/userHome/userhome4/kyumin/ANCE/MINDsmall_dev/news_title.csv', index = False)
#title_list = df['Title'].values.tolist()
#print(title_list[0:20])