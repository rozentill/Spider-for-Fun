
# -*- coding:utf-8 -*-
from tutorial.items import DmozItem

import scrapy
class DmozSpider(scrapy.spiders.Spider):

    name = "dmoz"#necessary

    allowed_domains = ["dmoz.org"]

    start_urls = [#necessary
        "http://www.dmoz.org/Computers/Programming/Languages/Python/"
    ]

    def parse(self,response):
        for href in response.css("ul.directory.dir-col > li > a::attr('href')"):
            url = response.urljoin(response.url, href.extract())
            yield scrapy.Request(url, callback=self.parse_dir_contents)


    def parse_dir_contents(self, response):#necessary
        # filename = response.url.split("/")[-2]#最后一个是“，所以倒数第二个分别是Books 和 Resources
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        for sel in response.xpath('//ul/li'):
            item = DmozItem() # 自定义的字典
            item['title'] = sel.xpath('a/text()').extract()
            item['link'] = sel.xpath('a/@href').extract()
            item['desc'] = sel.xpath('text()').extract()
            yield item
