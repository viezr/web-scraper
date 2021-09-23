# Keywords to filter output data
keywords = [ "альфа", "райф", "россельхоз", "рсхб", "росбанк",
             "газпромбанк", "гпб", "кита", "кнр", "fxcn", "fxus",
             "vtbx", "galaxy s21", "iphone 12", "pixel 4", "etf" ]

# Sites for scrapping. Name and type used to choice logic
sites = [
    #{ "name": "amazon.com", "type": "bestsellers",
    #    "path": "/gp/bestsellers/electronics/7072561011" },
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
        "path": "/organization_Agentstvo_po_strakhovaniju_vkladov" },
    { "name": "etfunds.ru", "type": "news",
        "path": ""}
]
