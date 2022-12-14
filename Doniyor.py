# -*- coding: utf-8 -*-
"""3kun.uz_iktisodiyot.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1erHQmJmqQyPZ41FU9nBI52__0qUpK7t8
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
from multiprocessing import Pool
# from time import sleep
# from requests.adapters import HTTPAdapter
# from urllib3.util.retry import Retry
# session = requests.Session()
# retry = Retry(connect=3, backoff_factor=0.5)
# adapter = HTTPAdapter(max_retries=retry)
# session.mount('http://', adapter)
# session.mount('https://', adapter)

# session.get(url)

import backoff

@backoff.on_exception(
    backoff.expo,
    requests.exceptions.RequestException,
    max_tries=5,
    giveup=lambda e: e.response is not None and e.response.status_code < 500
)
def publish(self, data):
    r = requests.post(url, timeout=10, json=data)
    r.raise_for_status()

start_url = 'https://kun.uz/uz/news/category/iktisodiet?next='

def get_next_page_link(start_url):
  response = requests.get(start_url)
  soup = BeautifulSoup(response.text, "lxml")
  next_page_link = soup.find('a', class_='load-more__link').get('href')
  return f"https://kun.uz{next_page_link}"

count = 263
next_pages_urls = []
for _ in range(1, count+1):
  next_pages_urls.append(start_url)
  next_link = get_next_page_link(start_url)
  start_url = next_link

def get_page_data(url):
  response = requests.get(url)
  soup = BeautifulSoup(response.text, 'lxml')
  page_data = soup.find_all('div', class_ = 'col-md-4 mb-25 l-item')
  return page_data

data_for_df ={'News_title':[], 'News_text':[]}

def results(page_data):
   for data in page_data:
    news_title =data.find_all('a', class_="news__title")[0].text 
    data_for_df['News_title'].append(news_title)

allnews_url=[]
def results2(page_data):
 for data in page_data:
  sleep(2)
  news_url = 'https://kun.uz'+data.find_all('a')[0].get('href')
  allnews_url.append(news_url)
 for news in allnews_url:
  sleep(2)
  response = requests.get(news)
  soup = BeautifulSoup(response.text, 'lxml')
  data = soup.find('div', class_="single-layout__center slc")
  texts = data.find_all('p')
  content=''
  for text in texts:
    content += text.text
  data_for_df['News_text'].append(content)

# def make all():
# for url in next_pages_urls:
#   results(get_page_data(url))
#   results2(get_page_data(url))

def make_all(url):
  results(get_page_data(url))
  results2(get_page_data(url))

with Pool(10) as p:
  p.map(make_all, next_pages_urls)

df = pd.DataFrame(data_for_df)
df.shape
df.head()

pip install openpyxl

df.to_excel('kun_uz_itisodiyot.xlsx', encoding='utf-8', index=False)

df.to_csv('kun_uz_itisodiyot.csv', sep=';', encoding='utf-8', index=False)