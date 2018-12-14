import requests
from bs4 import BeautifulSoup


r = requests.get('https://rafaelmarques.mobi')
bs = BeautifulSoup(r.content, 'html.parser')

print(f'Blog title: {bs.title.string}')

content_box = bs.find('div', {'id': 'content_box'})
articles = content_box.find_all('article', class_='latestPost')

for article in articles:
    title = article.find('span', class_='p-name')
    if not title:
        continue
    
    url = article.find('a')['href']
    excerpt = article.find('div', class_='front-view-content')

    print(f'{title.get_text()}: {url}')
    print(f'Excerpt: {excerpt.get_text()} \n')
