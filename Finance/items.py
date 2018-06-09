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
    publish_user_href=scrapy.Field()
    reply_nodes=scrapy.Field()
    topicid=scrapy.Field()
    url=scrapy.Field()
    read_count=scrapy.Field()
    reply_count=scrapy.Field()
    stockcode=scrapy.Field()
    other_info=scrapy.Field()


class forumhtmlpage(scrapy.Item):
    board=scrapy.Field()
    mainurl=scrapy.Field()
    datetime=scrapy.Field()#unknown
    timestrimp=scrapy.Field()
    content=scrapy.Field()
    publish_time=scrapy.Field()
    spider_time=scrapy.Field()
    id=scrapy.Field()

class DFCFWpublisher(scrapy.Item):
    publish_user_href=scrapy.Field()
    publish_user_name=scrapy.Field()

class DFCFWpersionInfo(scrapy.Item):
    publish_user_name=scrapy.Field()
    publish_user_href=scrapy.Field()
    zixuan_num=scrapy.Field()
    guanzhu_num=scrapy.Field()
    fensi=scrapy.Field()
    influence_data=scrapy.Field()
    forumage=scrapy.Field()
    register_time=scrapy.Field()
    attention_field=scrapy.Field()
    attention_field_url=scrapy.Field()
    persion_abstract=scrapy.Field()

class forumIndexPage(scrapy.Item):
    mainurl = scrapy.Field()
    datetime = scrapy.Field()
    timestrimp = scrapy.Field()
    content = scrapy.Field()
