#!/usr/bin/env python3
'''
Base module for scraping sites
'''
import os
from urllib import request
from re import sub
from modules.useragents import ua
from random import randrange
from config import cache_folder, load_from_file


class Scraper:
    '''
    Base class for scraping sites
    '''
    def scraper(self) -> [str, None]:
        '''
        Scraper method. Return list of scraped data
        '''
        url = f"{self.host}{self.path}"
        site_name = sub("(http)s?:\/\/(www)?[.]?","", self.host)
        fname = sub("\W","_", site_name + self.path).lower()
        file = f"{cache_folder}{fname}.html"
        print("Parsing", url, "...")

        content = None
        # For debug. Load content from file instead of request each time.
        if load_from_file and os.path.isfile(file):
            with open( file, mode="r" ) as f:
                content = f.read()
        else:
            content = self._request_save(url, file)

        if content:
            data_list = self.parse(content)
            return {"site": site_name, "data": data_list}
        print("  ERROR. No content.")
        return None

    def _request_save(self, url, file) -> [str, None]:
        '''
        Request site and save to cache dir. Return site content
        '''
        content = None
        headers = {"User-Agent" : ua[randrange(len(ua))]}
        req = request.Request(url, headers=headers)
        try:
            with request.urlopen(req) as f:
                content = f.read().decode("utf-8")
        except:
            print("  ERROR. ConnectionError.")
        if not os.path.exists(cache_folder):
            os.makedirs(cache_folder)
        if content:
            with open(file, mode="w") as fd:
                fd.write(content)
        return content

