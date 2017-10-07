import scrapy
from scrapy.spider import spiders
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
import re
import requests
import json
import redis




class DFCFW_persion_info(scrapy.Spider):
    name = 'DFCFW_persion'
    allowed_domains=['eastmoney.com']
    urls = [
        'http://www.eastmoney.com/'
    ]

    headers={
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36',
        'Accept-Language':'zh-CN,zh;q=0.8',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'
    }


    def start_requests(self):
        for url in self.urls:
            yield scrapy.Request(url=url,headers=self.headers,callback=self.create_uid_from_mongodb)

    def create_uid_from_mongodb(self):
        client=redis.Redis(host='localhost',port=6379)