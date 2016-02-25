#!/usr/bin/env python
#-*-coding:utf8-*-

import re
import requests

url = 'https://pt.sjtu.edu.cn/torrents.php?inclbookmarked=0&incldead=0&spstate=0&cat=429&page=0'

class spider:


    def __init__(self):

        self.url = url

        print "start crawling ..."

    def getContent(self):

        response = requests.get(self.url)

        return response.content

    # def getEachLesson(self,):



if __name__=='__main__':

    putaospider = spider()

    print putaospider.getContent()
