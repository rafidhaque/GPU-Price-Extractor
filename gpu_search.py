from bs4 import BeautifulSoup
import requests
import re

# gpu = 3080
gpu = input('you are searching for... ')

url = f"https://www.newegg.com/p/pl?d={gpu}&N=4131"

page = requests.get(url).text

doc = BeautifulSoup(page, 'html.parser')

page_text = doc.find(class_='list-tool-pagination-text')
pages = int(str(page_text.find('strong')).split('>')[3][:-8])

# print(pages)

for page in range(1, pages+1):
    url = f"https://www.newegg.com/p/pl?d={gpu}&N=4131&page={page}"
    page = requests.get(url).text
    doc = BeautifulSoup(page, 'html.parser')

    items = doc.find_all(class_= 'item-cell')
    # print(items)

    for item in items:
        thing = item.find(class_= 'item-title', text=re.compile(gpu))
        thing = str(thing).split('>')
        if len(thing) > 1:
            name = (thing[1][:-3])
            price = item.find(class_= 'price-current')
            price = (price.find('strong'))
            price = str(price).split('>')[1][:-8]
            print(name +", " + price)