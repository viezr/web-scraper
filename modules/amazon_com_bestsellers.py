#!/usr/bin/env python3
'''
Module for scrapping prices from site amazon.com "Best sellers"
https://www.amazon.com/gp/bestsellers/electronics/7072561011
'''
from bs4 import BeautifulSoup
import datetime as dt


def logic(content):
    '''
    Return list of news [{date: date object, title: string, link: string}, ... ]
    '''
    soup = BeautifulSoup(content, "html.parser")
    news = soup.find("ol", {"id": "zg-ordered-list"})
    news = news.find_all("li")

    news_list = []
    item_count = 0
    for child in news:
        news_list.append({"title":""})
        news_list[item_count]["link"] = "https://www.amazon.com" + child.div.a['href']
        for block in child.div.a:
            for block2 in block:
                if block.name and block.string:
                    news_list[item_count]["title"] += block.string.strip().replace("\n","")
        news_list[item_count]["date"] = dt.date.today()

        for block in child:
            price = block.find_all("span",{"class": "a-color-price"})
            news_list[item_count]["title"] += str( " Price: " +
                price[0].span.string.strip().replace("\n","") )

        item_count += 1
    return news_list
