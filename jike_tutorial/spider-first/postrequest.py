#!/usr/bin/env python
#-*-coding:utf8-*-

import requests
import re

__author__ = 'Ryan Yao'

############################################################################
# References:
#https://www.zhihu.com/question/29755376
#http://docs.python-requests.org/en/latest/user/advanced/#session-objects
#https://segmentfault.com/q/1010000002421571
############################################################################


zhihu_url = 'https://www.zhihu.com/question/20684684#answer-29803622'

post_data = {
    'method': 'next',
    'params': '{"url_token":20684684,"pagesize":20,"offset":40}',
    '_xsrf': '950c4e7c23eb2dba772b892adf2c5d04'
}

headers = {
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36',
    'X-Requested-With': "XMLHttpRequest",
    'Referer': 'http://www.zhihu.com',
    'Host': 'www.zhihu.com'
}

# sourcecode = requests.post(zhihu_url,data=post_data,headers=headers).text
response = requests.get(zhihu_url)
sourcecode = response.text

results = re.findall('<a class=\"author-link\" data-tip=\"p\$t\$.*?\" href=\"/people/.*?\">(.*?)</a>',sourcecode,re.S)

for each in results:
    print each

print sourcecode