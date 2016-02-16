#-*-coding:utf8-*-

import re
import requests

f = open('text.txt','r')
html = f.read()
f.close()

result_imgwrap = re.findall('<div class="imgwrap"><img src="(.*?)"',html,re.S)
i=0
for url in result_imgwrap:
    print "Downloading : "+url
    pic = requests.get(url)
    fp = open('pic\\' + str(i) + '.jpg','wb')
    fp.write(pic.content)
    fp.close()
    i += 1

