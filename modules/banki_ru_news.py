#!/usr/bin/env python3
'''
Module for scraping news from site banki.ru
'''
from bs4 import BeautifulSoup
from utils.date_parser import convert_date
from modules.base_module import Scraper


class Banki_news(Scraper):
    def __init__(self, path):
        self.host = "https://banki.ru"
        self.path = path

    def parse(self, content):
        '''
        Return list of news [{date: date object, title: string, link: string}, ... ]
        '''
        soup = BeautifulSoup(content, "html.parser")
        news = soup.find("div", {"data-test": "news-lenta-list"})

        news_list = []
        item_count = 0
        for child in news.descendants:
            if child.name == "time":
                news_list.append({})
                news_list[item_count]["date"] = convert_date(child.string.strip())
            if child.name == "a":
                try:
                    if "text-list-link" in child["class"]:
                        try:
                            news_list[item_count]
                        except:
                            news_list.append({})
                            news_list[item_count]["date"] = news_list[item_count - 1]["date"]
                        news_list[item_count]["title"] = child.string.strip().replace("\n","")
                        news_list[item_count]["link"] = self.host + child["href"]
                        item_count += 1
                except:
                    pass
            try:
                if child["data-test"] == "news-exclusive-widget":
                    break
            except:
                pass

        return news_list
