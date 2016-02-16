#-*-coding:utf8-*-

import requests
import re

zhihu_url = 'https://www.zhihu.com/question/20684684#answer-29803622'

post_data = {
    'method': 'next',
    'params': '{"url_token":20684684,"pagesize":20,"offset":40}',
    '_xsrf':'950c4e7c23eb2dba772b892adf2c5d04'
}

sourcecode = requests.post(zhihu_url,data=post_data).text

results = re.findall('<a class="author-link" data-tip="p$t$(.*?)" href="/people/(.*?)">(.*?)</a>',sourcecode,re.S)

for each in results:
    print each

