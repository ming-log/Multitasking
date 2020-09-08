# __author__:"Ming Luo"
# date:2020/9/8

import requests
from lxml import etree

url = "https://www.douyu.com/g_yz"


def fetch(url):
    """请求并下载网页"""
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.26 Safari/537.36"
    headers = {'User-Agent': user_agent}
    r = requests.get(url, headers=headers)
    if r.status_code != 200:
        r.raise_for_status()
    return r.text


