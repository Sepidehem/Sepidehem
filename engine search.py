
from bs4 import BeautifulSoup
import requests
import lxml
import json

headers = {
  'User-agent':
  "Mozilla/5.0 (Windows NT 10.0; Win6a4; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582"
}

name = input("What to search?")
url = "https://www.target.com/s?searchTerm=" + name
html = requests.get(url, headers=headers).text

soup = BeautifulSoup(html, 'lxml')

print(url)
print(soup)
