# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FinanceItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass



class forumdata(scrapy.Item):
    content=scrapy.Field()
    publish_user=scrapy.Field()
    publish_time=scrapy.Field()
    data_proper=scrapy.Field()
    publish_user_href=scrapy.Field()
    reply_nodes=scrapy.Field()
    topicid=scrapy.Field()
    url=scrapy.Field()

