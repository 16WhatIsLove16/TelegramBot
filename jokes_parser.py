import requests
import random
from bs4 import BeautifulSoup as b


URL = 'https://www.anekdot.ru/'


def parser(url):
    r = requests.get(url)
    soup = b(r.text, 'html.parser')
    jokes = soup.find_all('div', class_='text')
    return [c.text for c in jokes]

list_of_jokes = parser(URL)
random.shuffle(list_of_jokes)