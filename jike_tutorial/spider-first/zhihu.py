#!/usr/bin/env python
#-*-coding:utf8-*-

import re
import requests
import lxml

html=requests.get('https://zhihu.com')

print html.content