#_*_coding:utf-8_*_
import scrapy
import scrapy_redis
from scrapy_redis.spiders import CrawlSpider
from scrapy.spiders import Rule
from scrapy.linkextractor import LinkExtractor
from scrapy.loader import ItemLoader
from Finance.items import forumhtmlpage
import datetime
import time





class eastmoney_page(CrawlSpider):
    name = 'eastmoney_page'
    allowed_domains = ['eastmoney.com']
    # start_urls = ['http://www.eastmoney.com/','http://guba.eastmoney.com/default,{},f_1.html.html'.format(str(i) for i in range(2,527207))]
    start_urls = ['http://guba.eastmoney.com/default_{}.html'.format(str(i)) for i in range(21000,527207)]


    rules = (
        Rule(LinkExtractor(allow=r'.*?eastmoney.com/list\,.*'), callback='parse_item', follow=False),#True该False
        Rule(LinkExtractor(allow='http://guba.eastmoney.com/news\,\d{6}\,\d{8,10}[_\d]\.html'),callback='deal_page_contain_content',follow=False),#True该False
        # Rule(LinkExtractor(allow='http://guba.eastmoney.com/default_\d*.html'),callback='parse_item',follow=False),#True改False
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


    def deal_page_contain_content(self,response):
        itemloader1=ItemLoader(response=response,item=forumhtmlpage())
        itemloader1.add_value('mainurl',response.url)
        itemloader1._add_value('datetime',datetime.datetime.now().strftime('%y-%m-%d %H:%M:%S'))
        itemloader1.add_value('timestrimp',time.time())
        itemloader1.add_value()