#! /usr/env/bin
#-*-coding:utf8-*-

import re
import requests
import datetime
from bs4 import BeautifulSoup

html = requests.get('https://ideas.repec.org/p/ags/aare93/171370.html')

soup = BeautifulSoup(html.content, 'html.parser')

# p = soup.find('div',{'class': 'related-research'}).p.find
#
# print p.find_all('a')
basic_url = 'https://ideas.repec.org'

def conference_parse(url):
    resp = requests.get(url)
    print 'Get the conference/journal page.'
    soup = BeautifulSoup(resp.content, 'html.parser')
    paperlist = soup.find_all('ul',{'class':'paperlist'})
    for pl in paperlist:
        li = pl.find_all('li')

        for paper in li:
            paper_url = paper.b.a.get('href')
            print 'Capture a paper.' + paper_url
            # return basic_url+paper_url
            # return parser(basic_url+paper_url)

conference_parse('https://ideas.repec.org/s/pkp/abetsr.html')

# paperlist = soup.find('div',{'id':'biblio-body'}).find_all('tr')[1].find('td',{'class':'va-middle'})

# year = re.compile(r'\d+')
# print int(year.findall(paperlist.text)[0])