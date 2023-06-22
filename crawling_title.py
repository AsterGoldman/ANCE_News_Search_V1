import requests
from bs4 import BeautifulSoup

def crawl_cnn_titles():
    url = 'https://www.cnn.com/'
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        #titles = soup.find_all('span', class_='cd__headline-text')
        titles = soup.find_all('span')

        for title in titles:
            print(title.text.strip())

    else:
        print('Failed to retrieve CNN page.')

crawl_cnn_titles()
