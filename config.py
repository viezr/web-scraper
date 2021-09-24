# For debug. Load content from file instead of request each time.
# If file not exist, it will request data from site
load_from_file = True

# cache folder will be created if not exist
cache_folder = "cache/"

# Keywords to filter output data
keywords = [ "кита", "кнр", "fxus", "galaxy s21", "iphone 12",
             "pixel 4", "etf", "u.s." ]

# Sites for scrapping. Name and type used to choice logic
sites = [
    { "name": "nytimes.com", "type": "news",
        "path": "/section/world" },
    { "name": "amazon.com", "type": "hotnew",
        "path": "/gp/new-releases/electronics/7072561011" },
    { "name": "e-katalog.ru", "type": "items",
        "path": "/SAMSUNG-GALAXY-S21-128GB.htm" },
    { "name": "banki.ru", "type": "news",
        "path": "/news/lenta/banks" },
    { "name": "banki.ru", "type": "news",
        "path": "/news/lenta/market" },
    { "name": "banki.ru", "type": "news",
        "path": "/news/lenta/world" },
    { "name": "investfunds.ru", "type": "news",
        "path": "/news/?action=search&stocks=1" },
    { "name": "investfunds.ru", "type": "news",
        "path": "/news/?action=search&bonds=1" },
    { "name": "ria.ru", "type": "news",
        "path": "/world" },
    { "name": "etfunds.ru", "type": "news",
        "path": ""}
]
