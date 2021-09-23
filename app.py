#!/usr/bin/env python3
"""
Web scraper with functions:
    - get list of data from specific site
    - search keywords in data
    - remove dublicates of domains, and dublicates of data per domain
    - generate simple html of data (full or filtered by keywords)
    - may be extended by adding new modules with logic for specific sites
"""
from modules.main_scraper import Scraper
from modules import ria_ru_news
from modules import banki_ru_news
from modules import investfunds_ru_news
from modules import etfunds_ru_news
from modules import ekatalog_ru_items
from modules import amazon_com_bestsellers
from utils.data_filter import filter_data
from utils.html_generator import generate_html
from config import keywords
from config import sites


'''
Init scraping set for sites (site, path, parse module)
'''
logics = {
    "amazon.com": { "host": "https://www.amazon.com",
                    "bestsellers": amazon_com_bestsellers.logic,
                    "hotnew": amazon_com_bestsellers.logic },
    "e-katalog.ru": { "host": "https://www.e-katalog.ru",
                      "items": ekatalog_ru_items.logic },
    "banki.ru": { "host": "https://www.banki.ru",
                  "news": banki_ru_news.logic },
    "investfunds.ru": { "host": "https://investfunds.ru",
                        "news": investfunds_ru_news.logic },
    "ria.ru": { "host": "https://ria.ru",
                "news": ria_ru_news.logic },
    "etfunds.ru": { "host": "https://etfunds.ru",
                    "news": etfunds_ru_news.logic }
}

# Create for parsed data
data_list = []
# For debug. Load content from file instead of request each time.
load_from_file = True
if load_from_file:
    print("\nINFO: Loading content from files cache. Request only if no file\n")

for site in sites:
    sname = site["name"]
    stype = site["type"]
    sc = Scraper(logics[sname]["host"], site["path"], logics[sname][stype])
    data_list.append(sc.scraper(load_from_file) )

#Filter data by keywords (may be omited for only remove dublicates), remove dublicates
data_list = filter_data(data_list, keywords)

#Generate html file. Data filter not necessary, just for information on site
generate_html(data_list, keywords)

