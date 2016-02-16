#-*-coding:utf8-*-

####################
#       常用方法    #
#findall,Search,Sub#
####################

import re

secret_code = 'xxixxcxxlovexxsaadxxyouxxaax'

# . usage
a = 'xz123'
b = re.findall('x.',a)
print b

# * usage
a = 'xyxyxx123'
b = re.findall('x*',a)
print b

# 括号作为数据返回
# . 不匹配换行符,但加上re.S可以匹配换行符

result = re.findall('xx(.*?)xx',secret_code)
for i in result:
    print i


#search找到第一个即返回  re.search(pattern, string, flags)

#sub 替换匹配项 re.sub(pattern, repl, string, count)



def hello():
    print 'hello,world'

