# __author__:"Ming Luo"
# date:2020/9/8
import os
import requests
from lxml import etree
import threading
import queue
import time

q = queue.Queue()
page_num = 2

def download_url(url, type_='content'):
    """下载页面"""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko'}
    r = requests.get(url, headers=headers)
    if type_ == 'text':
        return r.text
    return r.content

def get_img_url(start_url):
    """得到该页面所有的图片地址"""
    global page_num
    if page_num > 0:
        url_data = download_url(start_url, 'text')
        url_html = etree.HTML(url_data)
        img_url = url_html.xpath("//a[@class='thumbnail vpic_wrap']/img/@bpic")
        put_task(img_url)
        next_path = url_html.xpath("//a[@class='next pagination-item ']/@href")[0]
        next_url = 'https:' + next_path
        page_num = page_num - 1
        get_img_url(next_url)

def put_task(img_url):
    """将得到的图片地址加入的任务中"""
    if isinstance(img_url, list):
        for i in img_url:
            q.put(i)
    else:
        q.put(img_url)


def save_img(save_path):
    """从任务中提取图片地址并且，保存图片到本地"""
    while True:
        img_url = q.get()
        img_content = download_url(img_url, 'content')
        img_name = img_url.split('/')[-1]
        img_path = os.path.join(save_path, img_name)
        print(img_path)
        with open(img_path, 'wb+') as f:
            f.write(img_content)
            print(img_name + '下载完毕！')


def main():
    start_url = 'http://tieba.baidu.com/f?kw=海贼王&ie=utf-8'
    save_path = 'img'
    thread_num = 5
    for i in range(thread_num):
        t = threading.Thread(target=save_img, args=(save_path, ))
        t.start()
    get_img_url(start_url)

if __name__ == '__main__':
    main()
