import requests
from bs4 import BeautifulSoup

url = 'https://www.cnn.com/'

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
links = soup.find_all('a')
res=[]
#for link in links:
#    temp=link.get_text('href')
#    if temp != "#":
#        res.append(temp.replace("href", " ").replace("\\nhref", " ").replace("\n", " ").strip())
#print(res)

def getlink():
    for link in links:
        temp=link.get_text('href')
        if temp != "#":
            res.append(temp.replace("href", " ").replace("\\nhref", " ").replace("\n", " ").replace("•", " ").replace("@", " ").strip())
    return res