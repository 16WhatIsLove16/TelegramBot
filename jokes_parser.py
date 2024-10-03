import requests
import random
from bs4 import BeautifulSoup as b


URL = 'https://www.anekdot.ru/'
flag = True


def jokes_parser(url):
    r = requests.get(url)
    soup = b(r.text, 'html.parser')
    jokes = soup.find_all('div', class_='text')
    final_jokes = []
    for joke in jokes:
        if joke.find('a', class_='next') is not None:
            temp = jokes_parser(f"{url}{joke.find('a', class_='next')['href']}")
            final_jokes.extend(temp)
        if len(joke.text) < 4096:
            final_jokes.append(joke.text)

    return final_jokes


if flag:
    list_of_jokes = jokes_parser(URL)
    random.shuffle(list_of_jokes)
    flag = False

