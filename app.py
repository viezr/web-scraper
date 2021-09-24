#!/usr/bin/env python3
'''
App for requesting data from sites and generate html with filtered data.
- get list of data from specific site
- search keywords in data
- remove dublicates of data per domain, and dublicates of domains
- generate simple html of data (full or filtered by keywords)
- may be extended by adding new modules with logic for specific sites
Search keywords and sites for scraping stored in config.py.
App will try to convert many date formats to date object, or return today.
Using simple data format: [date:date_object, title:str]
'''
from modules import Ria_news
from modules import Banki_news
from modules import Investfunds_news
from modules import Etfunds_news
from modules import Ekatalog_items
from modules import Amazon_items
from modules import Nytimes_news
from utils import filter_data
from utils import generate_html
from config import keywords, sites, load_from_file


#Init scraping set for sites (site, type, parse module object)
#It set all possible types and modules. Used sites and paths stored in config.py
logic_classes = {
    "nytimes.com": { "news": Nytimes_news },
    "amazon.com": { "bestsellers": Amazon_items, "hotnew": Amazon_items },
    "e-katalog.ru": { "items": Ekatalog_items },
    "banki.ru": { "news": Banki_news },
    "investfunds.ru": { "news": Investfunds_news },
    "ria.ru": { "news": Ria_news },
    "etfunds.ru": { "news": Etfunds_news }
}

if __name__ == "__main__":
    # Create list for parsed data
    data_list = []
    if load_from_file:
        print("\nINFO: Loading content from files. Request only if no file\n")

    for site in sites:
        sname, stype, spath = site.values()
        sc = logic_classes[sname][stype](spath)
        data_list.append(sc.scraper() )

    #Filter data by keywords (may be omited for only remove dublicates), remove dublicates
    data_list = filter_data(data_list, keywords)

    #Generate html file. Data filter not necessary, just for information on site
    generate_html(data_list, keywords)
