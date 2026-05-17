#!/usr/bin/python3

import os
import requests
import sys
import bs4
from bs4 import BeautifulSoup as bsf

index = 0

def get_content(web_url, prev_link):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
            'Accept': 'application/json, text/plain,*/*',
            'Refer': prev_link
            }
        response = requests.get(web_url, timeout=5, headers=headers)
        if response.status_code != 200:
            print("server not respond")
            print(f"Error: {response}")
            exit
        return response
    except requests.exceptions.RequestException:
        print(f"{web_url} : not a valid url")
    except requests.exceptions.Timeout:
        print("timeout")

def get_img_url_list(site_content):
    url_list = []
    soup = bsf(site_content, 'html.parser')
    url_list = [link.get("src") for link in soup.find_all('img')]
    return url_list

def get_content_type(url, prev_link):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
            'Accept': 'application/json, text/plain,*/*',
            'Refer': prev_link
            }
        r = requests.head(url, timeout=5, headers=headers)
        content_type = r.headers.get("Content-Type")
        return "." + content_type.split("/")[-1]
    except requests.exceptions.Timeout:
        print("timeout")
        return None

def down_img(img_url_list, prev_link, directory):
    global index
    SUPPORTED_FORMAT = [".jpg", ".jpeg", ".png", ".gif"]
    for link in img_url_list:
        type = get_content_type(link, prev_link)
        if type and type in SUPPORTED_FORMAT:
            fileName = directory+"/img_"+str(index)+type
            print (link)
            content = get_content(link,prev_link)
            if content:
                data = content.content
                with open(fileName,"wb") as file:
                    file.write(data)
            index += 1
  
def get_absolute_link(domain_name, relative_path):
    path = ""
    if relative_path[0:4] != 'http':
        if domain_name[-1] != '/':
            domain_name +='/'
        path = domain_name + relative_path
    else:
        path = relative_path
    return path

def check_two_param(lst_param):
    param =["-r", "-l", "-p"]
    if lst_param == param[:2]:
        return True
    elif lst_param == param[::2]:
        return True
    else:
        return False 

def check_three_param(lst_param):
    param =["-r", "-l", "-p"]
    if check_two_param(lst_param[1:3]):
        return check_two_param(lst_param[1:5:3])
    return False

def check_param(lst_param):
    param = ["-r", "-l", "-p"]
    if len(lst_param) == 3 and lst_param[1] == "-r":
        return True
    elif len(lst_param) == 5:
        return check_two_param(lst_param[1:3])
    elif len(lst_param) == 7:
        return check_three_param(lst_param)
    else:
        return False

def get_param(lst_param):
    my_dict = {}
    if "-l" in lst_param:
        my_dict["-l"] = lst_param[lst_param.index("-l") + 1]
    else:
        my_dict["-l"] = 5
    if "-p" in lst_param:
        my_dict["-p"] = lst_param[lst_param.index("-p") + 1]
    else:
        my_dict["-p"] = "data"
    my_dict["url"] = lst_param[-1]
    return my_dict

def get_sublink(url_content):
    url_list = []
    soup = bsf(url_content, 'html.parser')
    url_list = [link.get("href") for link in soup.find_all('a')]
    return url_list

def recursive_call(url_list, prev_link, depth, dir):
    if depth >= 1:
        for link in url_list:
            print(f"Entering: {link}")
            content = get_content(link, prev_link)
            if content:
                url_list = get_img_url_list(content.text)
                url = []
                for u in url_list:
                    new_url = get_absolute_link(link, u)
                    url.append(new_url)
                down_img(url, link, dir)
                sub_url_list = get_sublink(content.text)
                sub_url = []
                for u in sub_url_list:
                    if u:
                        sub_url.append(get_absolute_link(prev_link, u))
                recursive_call(sub_url, link, depth - 1, dir)

def main():
    if check_param(sys.argv) == False:
        print("usage: <./spider.py> [-rlp] URL")
        print("Option -l [N]: max of depth level of download, default 5 ")
        print("Option -p [PATH]: path to the downloaded file, default ./data/")
    else:
        param = get_param(sys.argv)
        os.makedirs(param["-p"], exist_ok=True)
        link = [param["url"]]
        try:
            int(param["-l"])
        except ValueError:
            print("Option -l takes integer as parameter")
            sys.exit()
        recursive_call(link, link[0], int(param["-l"]), param["-p"])


if __name__ == "__main__":
    main()
