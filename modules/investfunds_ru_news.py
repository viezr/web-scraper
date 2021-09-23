#!/usr/bin/env python3
'''
Module for scrapping news from site investfunds.ru
'''
from bs4 import BeautifulSoup
from utils.date_parser import convert_date


def logic(content):
    '''
    Return list of news [{date: date object, title: string, link: string}, ... ]
    '''
    soup = BeautifulSoup(content, "html.parser")
    news = soup.find("ul", {"class": "news_list"})
    news = news.find_all("li")

    news_list = []
    item_count = 0
    for child in news:
        if "date" in child["class"]:
            news_list.append({})
            news_list[item_count]["date"] = convert_date(child.string.strip())
        if "item" in child["class"]:
            try:
                news_list[item_count]
            except:
                news_list.append({})
                news_list[item_count]["date"] = news_list[item_count - 1]["date"]
            news_list[item_count]["title"] = child.a.string.strip().replace("\n","")
            news_list[item_count]["link"] = f"https://investfunds.ru{child.a['href']}"
            item_count += 1
    return news_list
