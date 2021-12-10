import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com/"
page = requests.get(url)
print(page.status_code)

soup = BeautifulSoup(page.content , 'html.parser')

data = []
author = []

quotes = soup.find_all(class_="quote")

for quote in quotes:
    data.append(quote.find(class_="text").get_text())
    author.append(quote.find(class_="author").get_text())

for word in data:
    print(word)