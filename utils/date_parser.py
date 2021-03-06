#!/usr/bin/env python3
'''
Date parser. Input string with 3 parts of YMD/DMY or 2 parts MD/DM,
with delimiters "-", "." and space. Month may be text (ru, en).
'''
import datetime as dt

def convert_text_month(month):
    '''
    Convert months to integer. Calls from convert_date
    '''
    months_en = ["jan", "feb", "mar", "apr", "may", "jun", "jul",
                 "aug", "sep", "oct", "nov", "dec" ]
    months_ru = ["янв", "фев", "мар", "апр", "май", "июн", "июл",
                 "авг", "сен", "окт", "ноя", "дек" ]
    try:
        month = int(month)
        return month
    except:
        if month in ["мая","мае","май"]:
            return 5
        if month[:3] in months_ru:
            return months_ru.index(month[:3]) + 1
        if month[:3] in months_en:
            return months_en.index(month[:3]) + 1
    return None

def convert_date(date):
    '''
    Convert string with date to datetime object
    '''
    if date == None:
        return dt.date.today()
    date = date.lower()
    if "сегод" in date or "today" in date:
        return dt.date.today()

    if "-" in date:
        date = date.split("-")
    elif "." in date:
        date = date.split(".")
    else:
        date = date.split()

    if len(date) == 1:
        return dt.date.today()

    if len(date) == 2:
        if len(date[0]) < 3:
            if convert_text_month(date[1]):
                date.append(str(dt.date.today().year))
        elif len(date[1]) < 3:
            month = convert_text_month(date[0])
            if month:
                date = [ str(dt.date.today().year), month, date[1] ]
        else:
            return dt.date.today()

    if len(date[2]) == 4:
        try:
            date = dt.date(int(date[2]), convert_text_month(date[1]), int(date[0]))
        except:
            date = dt.date.today()
    else:
        try:
            date = dt.date(int(date[0]), convert_text_month(date[1]), int(date[2]))
        except:
            date = dt.date.today()
    return date
