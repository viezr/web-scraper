# Web scraper
![image](screenshot.png)  
This app gets data from different sites and generates html with filtered data
and links. The app written in Python.  

## Features
- Get the list of data from specific site.
- Search keywords in data
- Remove dublicates of data per domain, and dublicates of domains.
- Generate simple HTML of data (full or filtered by keywords).
- Maybe extended by adding new modules with logic for specific sites.

## Notes
Search keywords and sites for scraping stored in config.py.
The app will try to convert many date formats to date objects or return today.
Using simple data format: `["date": date_object, "title": str, "link": str]`
