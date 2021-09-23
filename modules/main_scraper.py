#!/usr/bin/env python3
'''
Class module for scraping sites
'''
import requests
from re import sub
from os import path
from modules.useragents import ua
from random import randrange


class Scraper:
    '''
    Class for scraping sites
    '''
    def __init__(self, host, path, module):
        self.host = host
        self.path = path
        self.parse_module = module

    def scraper(self, file_save = False):
        '''
        Scraper method. Return list of scraped data
        '''
        request_url = f"{self.host}{self.path}"
        site_name = sub("(http)s?:\/\/(www)?[.]?","", self.host)
        fname = sub("\W","_", site_name + self.path).lower()
        file = f"cache/{fname}.html"
        print("Parsing", request_url, "...")

        def request_save():
            '''
            Request site and save to cache dir. Return site content
            '''
            hdr = { "User-Agent" : ua[randrange(len(ua))] }
            print(hdr)
            try:
                content = requests.get(request_url, headers=hdr, timeout=5).text
            except:
                raise ConnectionError
            f = open( file, mode="w" )
            f.write(content)
            f.close()
            return content

        if file_save:
            # For debug. Load content from file instead of request each time.
            if path.isfile(file):
                f = open( file, mode="r" )
                content = f.read()
                f.close()
            else:
                content = request_save()
        else:
                content = request_save()

        data_list = self.parse_module(content)

        return { "site": site_name, "data": data_list }
