#!/usr/bin/env python
#-*-coding:utf8-*-

import re
import requests

url = 'http://www.jikexueyuan.com/course/?pageNum='

class spider:


    def __init__(self):
        self.url = url
        return

    def getContent(self):

        response = requests.get(self.url)

        return response.content

    def 


if __name__=='__main__':

    jikespider = spider()

    print jikespider.getContent()
