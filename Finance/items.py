# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
import mongoengine
from mongoengine.document import Document
from mongoengine.fields import *
from mongoengine import connect


connect('21世纪教育网3', host="localhost", port=27017)


class FinanceItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class MongoItem(scrapy.Item):
    def __create_sqlalchemy_item__(self):
        if not "mongo_type" in self.__class__.__dict__.keys():
            raise Exception("没有指明一种数据类型,或这种数据类型本来就不存在！")
        type_instance = eval(self.mongo_type)()
        try:
            for _k in self.keys():
                # if _k != "picture":
                    type_instance.__setattr__(_k, self[_k])
                # else:
                #     type_instance.picture.put(self[_k])
        except Exception as e:
            raise e

        return type_instance


class Forum(MongoItem):
    mongo_type = "ForumMongo"
    content = scrapy.Field()
    publish_user = scrapy.Field()
    publish_time = scrapy.Field()
    publish_user_href = scrapy.Field()
    user_device = scrapy.Field()
    topic_id = scrapy.Field()
    url = scrapy.Field()
    read_count = scrapy.Field()
    reply_count = scrapy.Field()
    stock_code = scrapy.Field()
    other_info = scrapy.Field()
    forum_age = scrapy.Field()
    influence = scrapy.Field()


class RawHtml(MongoItem):
    mongo_type = "RawHtmlMongo"
    board = scrapy.Field()
    url = scrapy.Field()
    datetime = scrapy.Field()#unknown
    content = scrapy.Field()
    publish_time = scrapy.Field()
    spider_time = scrapy.Field()
    id = scrapy.Field()


class PublisherInfo(MongoItem):
    mongo_type = "PublisherInfoMongo"
    publish_user_id = scrapy.Field()
    publish_user_name = scrapy.Field()
    publish_user_href = scrapy.Field()
    zixuan_num = scrapy.Field()
    guanzhu_num = scrapy.Field()
    fans = scrapy.Field()  # 他的粉丝
    influence = scrapy.Field()  # 影响力
    forum_age = scrapy.Field()  # 吧龄
    register_time = scrapy.Field()  # 注册时间
    attention_field = scrapy.Field()  # 能力圈
    attention_field_url = scrapy.Field()
    abstract = scrapy.Field()
    visit_count = scrapy.Field()


class Replay(MongoItem):
    mongo_type = "ReplayMongo"
    replay_id = scrapy.Field()
    content = scrapy.Field()
    publish_user = scrapy.Field()
    publish_user_id = scrapy.Field()
    publish_time = scrapy.Field()
    publish_user_href = scrapy.Field()
    topic_id = scrapy.Field()
    influence = scrapy.Field()
    forum_age = scrapy.Field()


class RawHtmlMongo(Document):
    board = StringField()
    url = URLField()
    datetime = DateTimeField()
    content = StringField()
    publish_time = DateTimeField()
    spider_time = DateTimeField()
    id = StringField()

    meta = {
        "indexes":[
            "mainurl"
        ],
        "unique":True
    }


class ForumMongo(Document):
    content = StringField()
    publish_user = StringField()
    publish_time = DateTimeField()
    publish_user_href = URLField()
    user_device = StringField()  # from mobile phone
    topic_id = IntField()
    url = URLField()
    read_count = IntField()
    reply_count = IntField()
    stock_code = StringField()
    other_info = StringField()
    influence = FloatField()
    forum_age = FloatField()
    meta = {
        "indexes": []
    }


class ReplayMongo(Document):
    replay_id = StringField()
    content = StringField()
    publish_user_id = StringField()
    publish_user = StringField()
    publish_time = DateTimeField()
    publish_user_href = StringField()
    topic_id = StringField()  # 观点id
    influence = IntField()
    forum_age = FloatField()


class PublisherInfoMongo(Document):
    publish_user_id = StringField()
    publish_user_name = StringField()
    publish_user_href = URLField()
    zixuan_num = IntField()
    guanzhu_num = IntField()
    fans_count = IntField()  # 他的粉丝
    influence = FloatField()  # 影响力
    forum_age = FloatField()  # 吧龄
    register_time = DateTimeField()  # 注册时间
    attention_field = StringField()  # 能力圈
    attention_field_url = URLField()
    abstract = StringField()
    visit_count = IntField()


if __name__ == '__main__':
    pass

