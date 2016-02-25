#!/usr/bin/env python
#-*-coding:utf8-*-

from lxml import etree
import requests

#在chrome中审查元素直接右键copy xpath可以直接得到xpath

response = requests.get('www.hunantv.com')

print response.content