#!/usr/bin/env python3
'''
Module for scraping prices from site news.google.com
'''
from bs4 import BeautifulSoup
from utils.date_parser import convert_date
from modules.base_module import Scraper


class Nytimes_news(Scraper):
    def __init__(self, path):
        self.host = "https://www.nytimes.com"
        self.path = path

    def parse(self, content):
        '''
        Return list of news [{date: date object, title: string, link: string}, ... ]
        '''
        news_list = []
        item_count = 0

        soup = BeautifulSoup(content, "html.parser")
        news = soup.find("section", {"id": "collection-highlights-container"})
        if news:
            news = news.find_all("li")
            for child in news:
                if child.name:
                    news_list.append({})
                    news_list[item_count]["link"] = self.host + child.article.div.h2.a["href"]
                    news_list[item_count]["title"] = child.article.div.h2.a.string.strip().replace("\n","")
                    date = "-".join(child.article.div.h2.a["href"].split("/")[1:4])
                    news_list[item_count]["date"] = convert_date(date)
                item_count += 1

        news2 = soup.find("section", {"id": "stream-panel"})
        if news2:
            news2 = news2.find_all("li")
            for child in news2:
                if child.name:
                    news_list.append({})
                    news_list[item_count]["link"] = self.host + child.div.div.a["href"]
                    news_list[item_count]["title"] = child.div.div.a.h2.string.strip().replace("\n","")
                    news_list[item_count]["date"] = convert_date(None)
                item_count += 1

        if not news and not news2:
            print("  ERROR. Parsing fail, no blocks found")

        return news_list
