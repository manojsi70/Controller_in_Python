import requests
from bs4 import BeautifulSoup

def get_google_search_results(query, num_results=5):
    query = query.replace(' ', '+')
    url = f"https://www.google.com/search?q={query}&num={num_results}"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    response = requests.get(url, headers=headers)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')

    results = []
    for g in soup.find_all('div', class_='tF2Cxc', limit=num_results):
        title = g.find('h3').text
        link = g.find('a')['href']
        snippet = g.find('div', class_='VwiC3b').text
        results.append({'title': title, 'link': link, 'snippet': snippet})

    return results
