import scrapy
from scrapy_redis.spiders import RedisCrawlSpider
from scrapy.spiders import Rule
from scrapy.linkextractor import LinkExtractor
from scrapy.loader import ItemLoader
from Finance.items import RawHtml, Forum
import time
import pickle
import hashlib


class DFCFW_news(RedisCrawlSpider):
    name = 'DFCFW_news'

    rules = (
        Rule(LinkExtractor(allow=r'http\:\/\/finance\.eastmoney\.com\/news\/\d+\,\d.+\.html'), callback='parse_content_finance', follow=True),
        Rule(LinkExtractor(allow=r'http\:\/\/stock\.eastmoney\.com\/news\/\d+\,\d.+\.html'), callback='parse_content_stock', follow=True),
        Rule(LinkExtractor(allow=r'http\:\/\/guba\.eastmoney\.com\/news\,\w*?\,\d.+\.html'),
             callback='parse_forum', follow=True),
        Rule(LinkExtractor(allow=r'http\:\/\/guba\.eastmoney\.com\/news\,\S+\,\d.+\.html'),
             callback='parse_forum', follow=True),

        Rule(LinkExtractor(allow=r'.*?eastmoney\.com\/.*'), follow=True),

    )


    def parse_content_finance(self,response):

        def deal_publish_time(publish_time):
            print(publish_time)
            year_str=publish_time[0:4]
            mounth_str=publish_time[4:6]
            day_str=publish_time[6:8]

            return year_str+'-'+mounth_str+'-'+day_str+' 00:00:00'


        loader1=ItemLoader(response=response, item=RawHtml())
        loader1.add_value('board','DFCFW_finance')
        loader1.add_value('mainurl',response.url)
        loader1.add_value('timestrimp',int(time.time()*1000))
        loader1.add_value('content',response.text)
        loader1.add_value('publish_time',response.url.split(',')[-1].split('.')[0],deal_publish_time)
        loader1.add_value('spider_time',time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
        loader1.add_value('id',hashlib.md5(response.url.encode('utf-8')).digest())
        item1=loader1.load_item()
        return item1


    def parse_content_stock(self,response):

        def deal_publish_time(publish_time):
            print(publish_time)
            year_str=publish_time[0:4]
            mounth_str=publish_time[4:6]
            day_str=publish_time[6:8]

            return year_str+'-'+mounth_str+'-'+day_str+' 00:00:00'


        loader1=ItemLoader(response=response, item=RawHtml())
        loader1.add_value('board','DFCFW_stock')
        loader1.add_value('mainurl',response.url)
        loader1.add_value('timestrimp',int(time.time()*1000))
        loader1.add_value('content',response.text)
        loader1.add_value('publish_time',response.url.split(',')[-1].split('.')[0],deal_publish_time)
        loader1.add_value('spider_time',time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
        loader1.add_value('id',hashlib.md5(response.url.encode('utf-8')).digest())

        item1=loader1.load_item()
        return item1


    def parse_forum(self,response):

        def deal_publish_time(publish_time):
            print(publish_time)
            year_str = publish_time[0:4]
            mounth_str = publish_time[4:6]
            day_str = publish_time[6:8]

            return year_str+'-'+mounth_str+'-'+day_str+' 00:00:00'

        loader1 = ItemLoader(response=response, item=RawHtml())
        loader1.add_value('board','DFCFW_guba')
        loader1.add_value('mainurl',response.url)
        loader1.add_value('timestrimp',int(time.time()*1000))
        loader1.add_value('content',response.text)
        loader1.add_value('publish_time',time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
        loader1.add_value('spider_time',time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
        # loader1.add_value('id',hashlib.md5(response.url.encode('utf-8')).digest())

        item1=loader1.load_item()
        yield item1

        loader2 = ItemLoader(response=response, item1=Forum)


