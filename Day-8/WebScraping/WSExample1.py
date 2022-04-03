import requests
from bs4 import BeautifulSoup

URL = "https://www.microsoft.com/en-in/"

r=requests.get(URL)

soup = BeautifulSoup(r.content,'html5lib')

print(soup.prettify())
