#_*_coding:utf-8_*_
import scrapy


class testfile(scrapy.Spider):
    name = 'filespider'
    start_urls=['file://127.0.0.1//media/liang/Data/test/yourfile.txt']


    def parse(self, response):
        print (response.text)