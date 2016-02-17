#!/usr/bin/env python
#-*-coding:utf8-*-

import requests
import re
import sys

#使用定义headers来对抗反爬虫机制
test_headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.97 Safari/537.36'}

douban = requests.get('https://www.douban.com',headers = test_headers)

print douban.text
