from bs4 import BeautifulSoup
import requests

url = 'https://www.startech.com.bd/asus-phoenix-geforce-gtx-1650-oc-graphics-card'

result = requests.get(url)

doc = BeautifulSoup(result.text, 'html.parser')

prices = doc.find_all('div', text=lambda t: t and '৳' in t)
print(prices)