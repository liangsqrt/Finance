import scrapy
from scrapy_redis.spiders import RedisCrawlSpider
from scrapy.spiders import CrawlSpider
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from Finance.items import RawHtml, Forum, Replay, PublisherInfo
import time
import datetime
import hashlib
import json
from copy import deepcopy


class DFCFW_news(CrawlSpider):
    name = 'DFCFW_news'

    # 这里的顺序不能改变，redis中就靠顺序来定位callback。
    rules = (
        # Rule(LinkExtractor(allow=r'http\:\/\/finance\.eastmoney\.com\/\w.+\/\d*\.html'), callback='parse_content_finance', follow=False),
        # Rule(LinkExtractor(allow=r'http\:\/\/stock\.eastmoney\.com\/news\/\d+\,\d.+\.html'), callback='parse_content_stock', follow=False),
        Rule(LinkExtractor(allow=r'http\:\/\/iguba\.eastmoney\.com\/\d*'),
             callback="parse_person", follow=True),
        Rule(LinkExtractor(allow=r'http\:\/\/guba\.eastmoney\.com\/.*'), follow=True),


    )
    start_urls = [
        "http://guba.eastmoney.com/default,0_1.html",
        "http://guba.eastmoney.com/default,99_1.html",
    ]


    def parse_person(self, response):
        #  保存原始网页信息
        loader1 = ItemLoader(response=response, item=RawHtml())
        loader1.add_value('board', 'DFCFW_iguba')
        loader1.add_value('url', response.url)
        loader1.add_value('datetime', datetime.datetime.now())
        loader1.add_value('content', response.text)
        loader1.add_value('spider_time', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

        item1 = loader1.load_item()
        yield item1


    def parse_persne2(self, response):

        loader2 = ItemLoader(response=response, item=PublisherInfo())
        loader2.add_value("publish_user_href", response.url)
        loader2.add_xpath("publish_user_name", '//div[@class="taname"]/text()', lambda x: x[0].strip())
        loader2.add_xpath("influence", "//div[@id='influence']//span/@data-influence", lambda x: int(x[0]) if x else 0)
        loader2.add_xpath("publish_user_id",
                          "//div[@class='gbbody']//div[@class='tanums']//td/a[contains(@href, 'fans')]/em/../../a/@href",
                          lambda x: x[0].strip("/").strip("/fans") if x else "")
        loader2.add_value("his_stock_count",
                          response.xpath("//div[@class='gbbody']//div[@class='tanums']//td[1]/a/em/text()").extract_first(),
                          lambda x: int(x[0].strip()) if x else 0)
        loader2.add_xpath("fans_count",
                          "//div[@class='gbbody']//div[@class='tanums']//td/a[contains(@href, 'fans')]/em/text()",
                          lambda x: int(x[0].strip()) if x else 0)
        loader2.add_xpath("person_he_care_count",
                          "//div[@class='gbbody']//div[@class='tanums']//td/a[contains(@href, 'tafollow')]/em/text()",
                          lambda x: int(x[0].strip()) if x else 0)
        loader2.add_value("visit_count",
                          response.xpath('//div[@class="sumfw"]//span[contains(text(), "次")]/text()').extract_first(),
                          lambda x: x[0].strip("次") if x else 0)
        loader2.add_value("register_time", response.xpath("//div[@id='influence']//span[@style]").re("\((.*)\)"))
        loader2.add_value("forum_age", response.xpath("//div[@id='influence']//span/text()").extract_first(0))
        loader2.add_xpath("attention_field", '//div[@id="influence"]/a[@target]/text()')
        loader2.add_xpath("attention_field_url", '//div[@id="influence"]/a[@target]/@href')
        loader2.add_xpath("abstract", '//div[@class="taintro"]/text()')

        loader2.add_value("fans", response.url+"/fans")
        loader2.add_value("his_stock", "http://iguba.eastmoney.com/interf/stocklist.aspx")
        loader2.add_value("person_he_care", response.url + "/tafollow")

        item2 = loader2.load_item()
        yield item2


        # todo: fans,stock_focused_on 都需要在filepipeline中写ajax 请求吗，将剩下的字段补充完整。







