#!/usr/bin/env python3
'''
Module for scraping news from site e-katalog.ru
'''
from bs4 import BeautifulSoup
from utils.date_parser import convert_date
from modules.base_module import Scraper


class Ekatalog_items(Scraper):
    def __init__(self, path):
        self.host = "https://www.e-katalog.ru"
        self.path = path

    def parse(self, content):
        '''
        Return list of news [{date: date object, title: string, link: string}, ... ]
        '''
        soup = BeautifulSoup(content, "html.parser")
        main_block = soup.find("td", {"class": "main-part-content"})
        if not main_block:
            print("  ERROR. Parsing fail, no blocks found")
            return []

        title = main_block.find("h1", {"itemprop": "name"}).text.strip()
        price = main_block.find("span", {"itemprop": "lowPrice"})["content"]
        link = main_block.find("div", {"id": "item-bookmarks"}).a.next_sibling["href"]

        item_list = [{
            "date": convert_date("today"),
            "title": f"{title} - {price} rub.",
            "link": self.host + link
        }]

        return item_list
