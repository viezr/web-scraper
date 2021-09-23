#!/usr/bin/env python3
'''
Module for scrapping news from site ria.ru
'''
from bs4 import BeautifulSoup
from utils.date_parser import convert_date


def logic(content):
    '''
    Return list of news [{date: date object, title: string, link: string}, ... ]
    '''
    soup = BeautifulSoup(content, "html.parser")
    news = soup.find("div", {"class": "list-tags"})
    news = news.find_all("div", {"class": "list-item"})

    news_list = []
    item_count = 0
    for child in news:
        news_list.append({})
        date = child.div.next_sibling.div.string.strip()
        news_list[item_count]["date"] = convert_date(date.split(",")[0])
        link = str(child.div.a.next_sibling["href"])
        news_list[item_count]["title"] = child.div.a.next_sibling.string.strip().replace("\n","")
        news_list[item_count]["link"] = link
        item_count += 1
    return news_list
