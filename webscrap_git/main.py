import requests
from bs4 import BeautifulSoup as bs

github_user = input('Input for github user id: ')
url = 'https://github.com/'+github_user
r = requests.get(url)
soup =  bs(r.content, 'html.parser')
profile_img = soup.find('div', {'class':'details-overlay'})['details']
print(profile_img)