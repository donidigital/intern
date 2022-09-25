from bs4 import BeautifulSoup
import requests
import pickle
dict = {}
def script(url):
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, 'lxml')
    title = soup.find('div', class_="single-header__title")
    contents = soup.find_all('p')
    c = ''
    for content in contents:
        c+=content.text
    dict[title.text] = c

def page(big_url):
    html_text = requests.get(big_url).text
    soup = BeautifulSoup(html_text, 'lxml')
    news = soup.find_all('a', class_ = "news__title")

    for new in news:
        url = f"https://kun.uz{new['href']}"
        script(url)
    return soup.find('a', class_ = "load-more__link")['href']
big_url='https://kun.uz/uz/news/category/jahon'
for i in range(40):
    b = page(big_url)
    big_url = f"https://kun.uz{b}"




with open('saved_dictionary.pkl', 'wb') as f:
    pickle.dump(dict, f)