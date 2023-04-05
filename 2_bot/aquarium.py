from os import link
import requests
from bs4 import BeautifulSoup
import re


def currency(curr_name):
    url = 'https://www.takzdorovo.ru/db/nutritives/'
    response = requests.get(url)
    # print(response)

    soup = BeautifulSoup(response.text, 'html')
    # soup = str(soup)
    # print(response)

    quotes = soup.find_all('td')
    print(curr_name.capitalize())
    for i in range(len(quotes)):
        if curr_name.capitalize() == quotes[i].text:
            ind_el = i
            return (quotes[ind_el + 1].text)
        return ('В нашей базе нет такого продукта')




# print(quotes)
     # curr = input()