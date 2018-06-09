# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
# from scrapy.spiders import CrawlSpider, Rule
from scrapy.spiders import Rule
from scrapy_redis.spiders import RedisCrawlSpider
from scrapy.loader import ItemLoader
import re
import requests
import json
from Finance.items import forumdata
from Finance.items import forumhtmlpage
from Finance.items import DFCFWpublisher
import datetime
import time






# class CrawlSpider(CrawlSpider):
class CrawlSpider(RedisCrawlSpider):
    name = 'eastmoney'
    allowed_domains = ['eastmoney.com']
    # start_urls = ['http://www.eastmoney.com/','http://guba.eastmoney.com/default,{},f_1.html.html'.format(str(i) for i in range(2,527207))]
    start_urls = ['http://guba.eastmoney.com/default_{}.html'.format(str(i)) for i in range(1000,527207)]


    rules = (
        Rule(LinkExtractor(allow=r'.*?eastmoney.com/list\,.*'), callback='parse_item', follow=False),#True该False
        Rule(LinkExtractor(allow='http://guba.eastmoney.com/news\,\d{6}\,\d{8,10}[_\d]\.html'),callback='deal_page_contain_content',follow=False),#True该False
        Rule(LinkExtractor(allow='http://guba.eastmoney.com/default_\d*.html'),callback='parse_item',follow=False),#True改False
        # Rule(LinkExtractor(allow='http://guba.eastmoney.com/news\,\S{3,7}\,\d{8,10}[_\d]\.html'),callback='parse_item',follow=True),
        # Rule(LinkExtractor(allow='default,\d*,f_1.html'), callback='parse_item', follow=True),
    )
    domians='http://guba.eastmoney.com/'
    headers={
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding':'gzip, deflate',
        'Accept-Language':'zh-CN,zh;q=0.8',
        'Host':'guba.eastmoney.com',
        'Proxy-Connection':'closed',
        'Connection':'closed'
    }



    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url)#因为一定会经过的一个方法是parse，里边会根据rule中的设置获得对应的处理函数。

    def parse_item(self, response):
        i = {}
        print ('抓取到了一个list页面')
        print (response.status)
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        return i



    def deal_page_contain_content(self,response):
        forumdataItem=ItemLoader(response=response,item=forumdata())
        forumdataItem.add_xpath()