#!/usr/bin/env python3
'''
Functions for data filter by keywords, remove dublicates and sort by date
'''

def remove_dups(data_list):
    '''
    Remove dublicates of domains in list, and dublicates of data per site
    Calls from filter_data
    '''
    # uniqe list of sites names
    sites_arr = []
    for i in data_list:
        if not i["site"] in sites_arr:
            sites_arr.append(i["site"])

    # dublicate of sites
    for site_name in sites_arr:
        cnt_dups = [x for x in range(len(data_list)) if data_list[x]["site"] == site_name]
        if len(cnt_dups) > 1:
            upd_data = {"site": site_name, "data": []}
            for dup in cnt_dups[::-1]:
                for item in data_list[dup]["data"]:
                    upd_data["data"].append(item)
                data_list.pop(dup)
            data_list.append(upd_data)

    # dublicate of data per site
    for site in data_list:
        upd_data = []
        for i in site["data"]:
            if not upd_data:
                upd_data.append(i)
            else:
                match = 0
                for new_i in upd_data:
                    if new_i["title"] == i["title"]:
                        match += 1
                if match == 0:
                    upd_data.append(i)

        site["data"] = upd_data

    return data_list

def sort_list(data_list):
    '''
    Sort items by date. Calls from filter_data
    '''
    out_list = []
    for site in data_list:
        new_items = sorted(site["data"], key=lambda k: k["date"], reverse=True)
        out_list.append({ "site": site["site"], "data": new_items })

    return out_list

def filter_data(data_list, keywords):
    '''
    Function for filter input data list by search keywords
    Call remove_dups and sort_list
    '''
    out_list = []
    idx = 0
    for site in data_list:
        out_list.append({ "site": site["site"], "data": [] })
        for item in site["data"]:
            for word in keywords:
                if word in item['title'].lower():
                    out_list[idx]["data"].append(item)
                    break
        idx += 1

    out_list = remove_dups(out_list)
    out_list = sort_list(out_list)

    return out_list
