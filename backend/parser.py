# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import json
import re 

def parse(source:str, url:str, class_:str, title:str):
    d_news = {}
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    if url != "https://lenta.ru/":
        all_news = soup.findAll('a', class_=class_)
    else:
        all_news = soup.findAll('a', class_=class_[0])
        all_mini_news = soup.findAll('a', class_=class_[1])
    if url == "https://lenta.ru/":
        for news in all_news:
            h3 = news('h3')
            title =re.findall(r'>.+<', str(h3))
            title = title[0].replace('<','').replace('>', '')
            # print(title)
            d_news[title] = news['href']
            # меньшие новости
        titles = []
        for news in all_mini_news:
            span  = news('span')
            title =re.findall(r'>.+<', str(span))
            titles.append(str(title[0]).replace('<','').replace('>', ''))
            d_news[titles[-1]] = 'https://lenta.ru' + news['href']
    else:
        for news in all_news:
            title_news = news[title].replace('\\xa08', '').replace('\\xa0', '')
            d_news[title_news] = news['href'].replace('\\xa08', '').replace('\\xa0', '')\


    i = 0
    id_news = []
    new_news = []
    href_news = []
    real_news = []
    for news in d_news:
        id_news.append(i)
        new_news.append(news)
        href_news.append(d_news[news])
        i += 1
    news = json.loads(json.dumps((source,list(zip(id_news,new_news,href_news)))))
    return news

yandex_news = parse("Яндекс новости", "https://yandex.ru/", "news__item", 'aria-label')
ria_news = parse("Риа новости", "https://ria.ru/", "cell-list__item-link color-font-hover-only", 'title')
lenta_news = parse("Лента новости", "https://lenta.ru/", ['card-big _topnews _news','card-mini _topnews'], 'space')
