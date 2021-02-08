import requests
#позволяет работать с юрл запросом, дает всю инфу с сайта

from bs4 import BeautifulSoup as bs4
#помогает разбить инфу с сайта на блоки

#ЗАГОЛОВКИ инфа которая передается бразеру,отоброжаются данные по поводу пользоваеля посещащий вебсайт
#без заголовок ты бот или робот

headers  = {
    'accept': '*/*',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36 OPR/73.0.3856.344 (Edition Campaign 34)'
}

url = 'https://itproger.com'
session = requests.Session()

try:
    req = session.get(url, headers = headers)
    if req.status_code  == 200:
        soup = bs4(req.content, 'html.parser')
        divs = soup.find_all('div', attrs={'class': 'article'})
        for div in divs:
            title = div.find('a').text
            href = div.find('a')['href']
            print('{}  - https://itproger.com/{}'.format(title, href))
        print('ok')
    else:
        print('mistake')
except Exception:
    print('no such kind of website')


