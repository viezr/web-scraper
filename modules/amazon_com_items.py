#!/usr/bin/env python3
'''
Module for scraping prices from site amazon.com "Best sellers"
https://www.amazon.com/gp/bestsellers/electronics/7072561011
'''
from bs4 import BeautifulSoup
from utils.date_parser import convert_date
from modules.base_module import Scraper


class Amazon_items(Scraper):
    def __init__(self, path):
        self.host = "https://www.amazon.com"
        self.path = path

    def parse(self, content):
        '''
        Return list of news [{date: date object, title: string, link: string}, ... ]
        '''
        soup = BeautifulSoup(content, "html.parser")
        news = soup.find("ol", {"id": "zg-ordered-list"})
        if news:
            news = news.find_all("li")
        if not news:
            print("  ERROR. Parsing fail, no blocks found")
            return []

        news_list = []
        item_count = 0
        for child in news:
            news_list.append({"title":""})
            news_list[item_count]["link"] = self.host + child.div.a['href']
            for block in child.div.a:
                for block2 in block:
                    if block.name and block.string:
                        news_list[item_count]["title"] += block.string.strip().replace("\n","")
            news_list[item_count]["date"] = convert_date(None)

            for block in child:
                price = block.find_all("span",{"class": "a-color-price"})
                news_list[item_count]["title"] += str( " Price: " +
                    price[0].span.string.strip().replace("\n","") )

            item_count += 1
        return news_list
