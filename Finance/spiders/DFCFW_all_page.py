import scrapy
from scrapy_redis.spiders import  RedisCrawlSpider
from scrapy.spiders import Rule
from scrapy.linkextractors import  LinkExtractor
from scrapy.loader import ItemLoader
from Finance.items import RawHtml
import time
import pickle
import hashlib


class DFCFW_news(RedisCrawlSpider):
    name = 'DFCFW_all_page'
    # redis_key = 'DFCFW_news:start_urls'

    rules = (
        Rule(LinkExtractor(allow=r'.*?eastmoney\.com\/.*'),callback='parse_content',follow=True),
    )


    def parse_content(self,response):

        def deal_publish_time(publish_time):
            print(publish_time)
            year_str=publish_time[0:4]
            mounth_str=publish_time[4:6]
            day_str=publish_time[6:8]

            return year_str+'-'+mounth_str+'-'+day_str+' 00:00:00'

        def deal_board_info(url):
            try:
                urlbegin_board=url.split('.')[0].split('//')[1]
            except :
                urlbegin_board='UnkonwBoard'
            board_path= url.split('.com')[1].split('.htm')[0].split('?')[0].replace(',','/')
            board_path_strip= board_path.strip('/')
            if board_path_strip:
                return '/'+urlbegin_board+'/'+board_path_strip+'/'
            else:
                return '/'+urlbegin_board+'/'+'/Unknown/'



        loader1=ItemLoader(response=response, item=RawHtml())
        loader1.add_value('board',response.url,deal_board_info)
        loader1.add_value('mainurl',response.url)
        loader1.add_value('timestrimp',int(time.time()*1000))
        loader1.add_value('content',response.text)
        # loader1.add_value('publish_time',response.url.split(',')[-1].split('.')[0],deal_publish_time)
        loader1.add_value('publish_time',time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
        loader1.add_value('spider_time',time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
        loader1.add_value('id',hashlib.md5(response.url.encode('utf-8')).digest())
        item1=loader1.load_item()
        return item1