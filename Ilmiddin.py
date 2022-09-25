import csv
import time
import requests
from bs4 import BeautifulSoup

n = 333
header = ['Title', 'Description']

def parser(url, i):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find_all('div', class_='col-md-4 mb-25 l-item')
    for result in results:
        inner_url = 'https://kun.uz'+result.find('a', class_='news__title')['href']
        inner_page = requests.get(inner_url)
        inner_soup = BeautifulSoup(inner_page.content, 'html.parser')
        
        #Getting title and content of news
        try:
            title = inner_soup.find('div', class_='single-header__title').text
        except:
            title=''
        try:
            content = inner_soup.find('div', class_='single-content')
        except:
            content=''
        p_tags = content.find_all('p')
        description = ''
        for tag in p_tags:
            description += tag.text
        
        #Write title and content to csv file
        writer.writerow([title, description])
        
        #Wait 3 sec to avoid getting blocked
        time.sleep(1)
        
    if i == n:
        print('Program has finished')
    else:
        #Get new url from Load more button
        new_url ='https://kun.uz'+soup.find('a', class_='load-more__link')['href']
        i+=1
        parser(new_url, i)

with open('fan_texnika.csv', 'a', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    url = "https://kun.uz/uz/news/category/tehnologia"
    i=0
    parser(url, i)