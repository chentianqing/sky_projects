# -*- coding: utf-8 -*-

# @Project:   sky_projects
# @Time:      2021-02-08 17:11
# @Author  :    TianQing Chen
# @File    :    20210208-3.py
# @function :   线程
import time

def crawl_page(url):
    print("crawling {}".format(url))
    sleep_time = int(url.split('_')[-1])
    print(sleep_time)
    time.sleep(sleep_time)
    print("OK {}".format(url))


if __name__ == '__main__':
    urls = ['url_1', 'url_2', 'url_3', 'url_4']
    for url in urls:
        crawl_page(url)


