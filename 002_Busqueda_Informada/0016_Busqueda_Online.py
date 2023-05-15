import requests
from bs4 import BeautifulSoup

def search_web(query, url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = []
    for link in soup.find_all('a'):
        if query in link.get_text().lower():
            results.append(link.get('href'))
    return results

search_results = search_web('py', 'https://www.python.org')
for i in search_results:
    print(i)
