import scrapy
import scrapy_redis
from scrapy_redis.spiders import CrawlSpider


class eastmoney_page(CrawlSpider):
    name = 'eastmoney_page'

    def start_requests(self):
        for i in range(1,564214):
            yield scrapy.Request(url='http://guba.eastmoney.com/default_'+str(i)+'.html')

    def parse_content(self,response):
