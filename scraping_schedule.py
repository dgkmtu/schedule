from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup
import re
import schedule
import time

def job():
    try:
        html = urlopen('https://news.yahoo.co.jp/topics')
    except HTTPError as e:
        print(e)
    except URLError as e:
        print(e)

    else:
        
        bs = BeautifulSoup(html.read(), 'lxml')
        newsList = bs.find('div', {'class': 'topicsListAllMain'}).find_all('a')
    
        for news in newsList:
            if re.match('^(https://)', news.attrs['href']):
                print(news.get_text())
                print(news.attrs['href'])

#1時間毎にjobを実行
schedule.every(1).hours.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
