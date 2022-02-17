# import lybrary
import requests
from bs4 import BeautifulSoup

URL = 'https://auto.ria.com/uk/search/?indexName=auto,order_auto,newauto_search&year[0].gte=2019&categories.main.id=1&brand.id[0]=29&model.id[0]=293&country.import.usa.not=-1&price.currency=1&abroad.not=0&custom.not=1&page=0&size=20&scrollToAuto=32073395'
HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
    'accept': '*/*'
}

def get_html (url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r

def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('section', class_='ticket-item')


    # print(items)


    cars = []
    for item in items:
        cars.append({
            'Title': item.find('div', class_='item ticket-title').get_text(strip=True),
            'Link': item.find('a', class_='address').get('href'),
            'USD': item.find('span', class_='bold green size22').get_text(),
            'UAH': item.find('span', class_='i-block').get_text().replace('\xa0', ' '),
            'Sity': item.find('li', class_='view-location').get_text(strip=True).replace('(від)', ''),
            'Gas': item.find('li', class_='item-char').find_next('li').find_next('li').get_text(strip=True)


        })
        return cars
    # print(cars)
    # print(len(cars))



def pars():
    html = get_html(URL)
    if html.status_code == 200:
        get_content(html.text)
    else:
        print("Ошибка проверь Url страници!")

pars()


