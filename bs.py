from unittest import result
from bs4 import BeautifulSoup
import re

with open('index.html', 'r') as f:
    doc = BeautifulSoup(f, 'html.parser')

result = doc.find_all(text=re.compile("\$.*"), limit=1)
for tag in result:
    print(tag.strip())
