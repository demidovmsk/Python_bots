#Второй способ парсинга

from os import link
import requests
from bs4 import BeautifulSoup
import re


def currency(curr_name):
    url = 'https://www.cbr.ru/currency_base/daily/'
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html')
    # soup = str(soup)
    # print(response)

    quotes = soup.find_all('td')
    # print(quotes)
    # curr = input()

    # find_el = f'<td>{curr.title()}</td>'
    # print(type(quotes))
    print(curr_name.capitalize())
    for i in range(len(quotes)):
        # print(quotes[i].text)
        if curr_name.capitalize() == quotes[i].text:
            # print(i)
            ind_el = i
            return (quotes[ind_el + 1].text)  # print(quotes[ind_el + 1].text)
    return ('Нет такой валюты') # print('Нет такой валюты')


