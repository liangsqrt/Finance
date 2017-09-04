# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.loader import ItemLoader


class CrawlSpider(CrawlSpider):
    name = 'eastmoney'
    allowed_domains = ['eastmoney.com']
    start_urls = ['http://www.eastmoney.com/']

    rules = (
        Rule(LinkExtractor(allow=r'.*?eastmoney.com/.*'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        i = {}
        print response.status
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        return i
        print 'hello'


    def deal_page_contain_content(self):
        pass