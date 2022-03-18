from unittest import result
from bs4 import BeautifulSoup
import requests

with open('index.html', 'r') as f:
    doc = BeautifulSoup(f, 'html.parser')

result = doc.find_all(class_='btn-item')
print(result)