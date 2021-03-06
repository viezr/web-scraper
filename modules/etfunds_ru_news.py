#!/usr/bin/env python3
'''
Module for scraping news from site etfunds.ru
'''
from bs4 import BeautifulSoup
from utils.date_parser import convert_date
from modules.base_module import Scraper


class Etfunds_news(Scraper):
    def __init__(self, path):
        self.host = "https://www.etfunds.ru"
        self.path = path

    def parse(self, content):
        '''
        Return list of news [{date: date object, title: string, link: string}, ... ]
        '''
        def parse_block(news):
            nonlocal item_count
            for child in news:
                if child.name:
                    news_list.append({})
                    date = child.div.div.span.time.string.strip().split(".")
                    news_list[item_count]["title"] = child.div.h4.a.string.strip()
                    news_list[item_count]["link"] = child.div.h4.a['href']
                    date = f"{date[2]} {date[1]} {date[0]}"
                    news_list[item_count]["date"] = convert_date(date)
                    item_count += 1

        news_list = []
        item_count = 0

        soup = BeautifulSoup(content, "html.parser")
        news = soup.find("div", {"class": "pt-cv-timeline"})
        if news:
            news = news.find("div", {"class": "tl-items"})
        if news:
            news = news.find_all("div", {"class": "pt-cv-content-item"})
            parse_block(news)

        news2 = soup.find("div", {"class": "el-content uk-panel uk-margin-top"})
        if news2:
            news2 = news2.find_all("div", {"class": "tl-item-content"})
            parse_block(news2)

        if not news and not news2:
            print("  ERROR. Parsing fail, no blocks found")

        return news_list
