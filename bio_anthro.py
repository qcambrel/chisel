import requests
from bs4 import BeautifulSoup

user_agent = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
urls = ['http://www.economist.com/topics/biological-anthropology']
headers = {'User-agent': user_agent}
request = requests.get(urls[0], headers=headers)
soup = BeautifulSoup(request.content, "lxml")
data = soup.find_all('div', {'class': 'topic-page-item-list'})
print(data)