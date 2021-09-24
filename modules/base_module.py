#!/usr/bin/env python3
'''
Base module for scraping sites
'''
import os
import requests
from re import sub
from modules.useragents import ua
from random import randrange
from config import cache_folder, load_from_file


class Scraper:
    '''
    Base class for scraping sites
    '''
    def scraper(self):
        '''
        Scraper method. Return list of scraped data
        '''
        request_url = f"{self.host}{self.path}"
        site_name = sub("(http)s?:\/\/(www)?[.]?","", self.host)
        fname = sub("\W","_", site_name + self.path).lower()
        file = f"{cache_folder}{fname}.html"
        print("Parsing", request_url, "...")

        def request_save():
            '''
            Request site and save to cache dir. Return site content
            '''
            hdr = { "User-Agent" : ua[randrange(len(ua))] }
            print(hdr)
            try:
                content = requests.get(request_url, headers=hdr, timeout=7).text
            except:
                raise ConnectionError
            if not os.path.exists(cache_folder):
                os.makedirs(cache_folder)
            f = open( file, mode="w" )
            f.write(content)
            f.close()
            return content

        if load_from_file:
            # For debug. Load content from file instead of request each time.
            if os.path.isfile(file):
                f = open( file, mode="r" )
                content = f.read()
                f.close()
            else:
                content = request_save()
        else:
                content = request_save()

        data_list = self.parse(content)

        return { "site": site_name, "data": data_list }
