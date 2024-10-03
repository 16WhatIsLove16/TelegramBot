import requests
from bs4 import BeautifulSoup as b


URL = 'https://arh.kassir.ru'
final_result = []

def all_events_parser(url):
    result = []
    r = requests.get(url)
    soup = b(r.text, 'html.parser')
    events = soup.find_all('a', class_='recommendation-item_img-block')
    for event in events:
        result.append(f"{url}{event['href']}")
    return result


result = all_events_parser(URL)


for url in result:
    r = requests.get(url)
    soup = b(r.text, 'html.parser')
    events = soup.find_all('p', class_=None)
    for i, text in enumerate(events):
        if i == 0:
            final_result.append([text.text])
        else:
            final_result[-1].append(text.text)

print(final_result)



