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
    'params': {
        "url_token":20684684,
        "pagesize":20,
        "offset":40
    },
    '_xsrf': '950c4e7c23eb2dba772b892adf2c5d04'
}

headers = {
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36',
    'X-Requested-With': "XMLHttpRequest",
    'Referer': 'http://www.zhihu.com/question/20684684',
    'Host': 'www.zhihu.com',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Cookie': '_za=3a3aacc9-4899-4606-a7bc-ad608782c4df; _xsrf=950c4e7c23eb2dba772b892adf2c5d04; _ga=GA1.2.1607806643.1453477218; q_c1=735553abea5a40ac89818e967d94f28b|1455196456000|1441316395000; aliyungf_tc=AQAAANeyhgz2ZgUADcbkdB4bsccVbSDd; cap_id="N2Q5YjAwY2MxNTNkNDUwZGJhNGRkNzViODM5YmRmZjI=|1455715437|7d281ca21c2c387b9ec7f0065b59b9e3cf253a66"; z_c0="QUFCQXNTUWtBQUFYQUFBQVlRSlZUU3dEN0ZiUktneFdUUElmdUx5QmItR1JjbEk1SkVDVW9RPT0=|1455715884|5ffb903a844ee42a733057173e86b2190f37fbde"; n_c=1; __utmt=1; __utma=51854390.1607806643.1453477218.1455720839.1455784328.3; __utmb=51854390.4.9.1455784339460; __utmc=51854390; __utmz=51854390.1455784328.3.3.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmv=51854390.100-1|2=registration_date=20140116=1^3=entry_date=20140116=1'
}

# s = requests.session()
#
# login_data = {
#     'email': 'xxx',
#     'password': 'xxx'
# }
#
# s.post('https://www.zhihu.com/#signin',login_data,headers = headers)
#
# r = s.get('https://www.zhihu.com')

sourcecode = requests.post(zhihu_url,data=post_data,headers=headers).text
# response = requests.get(zhihu_url)
# sourcecode = response.text

# results = re.findall('<a class=\"author-link\" data-tip=\"p\$t\$.*?\" href=\"/people/.*?\">(.*?)</a>',sourcecode,re.S)

# for each in results:
    # print each

print sourcecode

# print r.cookies