import requests
from bs4 import BeautifulSoup as bs


username = input('Enter Your Username on GitHub: ')
profile = f'https://github.com/{username}'

req = requests.get(profile)
scraper = bs(req.content, 'html.parser')
profile_photo = scraper.find('img', {'alt': 'Avatar'})['src']
print(profile_photo)