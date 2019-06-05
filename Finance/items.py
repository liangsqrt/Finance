# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from mongoengine.document import Document
from mongoengine.fields import *
from mongoengine import connect
from scrapy.loader.processors import TakeFirst

connect('东方财富网', host="localhost", port=27017)


class FinanceItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class MongoItem(scrapy.Item):
    def __create_sqlalchemy_item__(self):
        if "mongo_type" not in self.__class__.__dict__.keys():
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
    content = scrapy.Field(output_processor=TakeFirst())
    publish_user = scrapy.Field(output_processor=TakeFirst())
    publish_time = scrapy.Field(output_processor=TakeFirst())
    publish_user_href = scrapy.Field(output_processor=TakeFirst())
    user_device = scrapy.Field(output_processor=TakeFirst())
    topic_id = scrapy.Field(output_processor=TakeFirst())
    url = scrapy.Field(output_processor=TakeFirst())
    read_count = scrapy.Field(output_processor=TakeFirst())
    reply_count = scrapy.Field(output_processor=TakeFirst())
    stock_code = scrapy.Field(output_processor=TakeFirst())
    other_info = scrapy.Field(output_processor=TakeFirst())
    forum_age = scrapy.Field(output_processor=TakeFirst())
    influence = scrapy.Field(output_processor=TakeFirst())


class RawHtml(MongoItem):
    mongo_type = "RawHtmlMongo"
    board = scrapy.Field(output_processor=TakeFirst())
    url = scrapy.Field(output_processor=TakeFirst())
    datetime = scrapy.Field(output_processor=TakeFirst())  # unknown
    content = scrapy.Field(output_processor=TakeFirst())
    publish_time = scrapy.Field(output_processor=TakeFirst())
    spider_time = scrapy.Field(output_processor=TakeFirst())
    id = scrapy.Field(output_processor=TakeFirst())


class PublisherInfo(MongoItem):
    mongo_type = "PublisherInfoMongo"
    publish_user_id = scrapy.Field(output_processor=TakeFirst())
    publish_user_name = scrapy.Field(output_processor=TakeFirst())
    publish_user_href = scrapy.Field(output_processor=TakeFirst())
    # zixuan_num = scrapy.Field(output_processor=TakeFirst())
    # guanzhu_num = scrapy.Field(output_processor=TakeFirst())
    fans = scrapy.Field(output_processor=TakeFirst())  # 他的粉丝
    influence = scrapy.Field(output_processor=TakeFirst())  # 影响力
    forum_age = scrapy.Field(output_processor=TakeFirst())  # 吧龄
    register_time = scrapy.Field(output_processor=TakeFirst())  # 注册时间
    attention_field = scrapy.Field(output_processor=TakeFirst())  # 能力圈
    attention_field_url = scrapy.Field(output_processor=TakeFirst())
    abstract = scrapy.Field(output_processor=TakeFirst())
    visit_count = scrapy.Field(output_processor=TakeFirst())
    his_stock_count = scrapy.Field(output_process=TakeFirst())
    stock_focused_on = scrapy.Field(output_processor=TakeFirst())
    person_he_care_count = scrapy.Field(output_processor=TakeFirst())
    fans_count = scrapy.Field(output_processor=TakeFirst())
    person_he_care = scrapy.Field(output_processor=TakeFirst())
    his_stock = scrapy.Field(output_processor=TakeFirst())


class Replay(MongoItem):
    mongo_type = "ReplayMongo"
    replay_id = scrapy.Field(output_processor=TakeFirst())  # 本条回复的id
    content = scrapy.Field(output_processor=TakeFirst())
    publish_user = scrapy.Field(output_processor=TakeFirst())
    publish_user_id = scrapy.Field(output_processor=TakeFirst())
    publish_time = scrapy.Field(output_processor=TakeFirst())
    publish_user_href = scrapy.Field(output_processor=TakeFirst())
    topic_id = scrapy.Field(output_processor=TakeFirst())  # 整个帖子的id
    influence = scrapy.Field(output_processor=TakeFirst())
    forum_age = scrapy.Field(output_processor=TakeFirst())
    replay_to = scrapy.Field(output_processor=TakeFirst())


class RawHtmlMongo(Document):
    board = StringField()
    url = URLField()
    datetime = DateTimeField()
    content = StringField()
    publish_time = DateTimeField()
    spider_time = DateTimeField()
    id = StringField()

    meta = {
        "indexes": [
            "url"
        ],
        "unique": True
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
    forum_age = StringField()
    meta = {
        "indexes": [
            "url",
            "topic_id"
        ],
        "unique": True
    }


class ReplayMongo(Document):
    replay_id = StringField()
    content = StringField()
    publish_user_id = StringField()
    publish_user = StringField()
    publish_time = DateTimeField()
    publish_user_href = StringField()
    topic_id = StringField()  # 观点id
    influence = FloatField()
    forum_age = StringField()
    replay_to = StringField()
    meta = {
        "indexes": [
            "topic_id",
            "replay_id",
            "publish_user"
        ],
        "unique": True
    }


class PublisherInfoMongo(Document):
    publish_user_id = StringField()
    publish_user_name = StringField()
    publish_user_href = URLField()
    # zixuan_num = IntField()
    # guanzhu_num = IntField()
    fans = ListField()  # 他的粉丝
    influence = FloatField()  # 影响力
    forum_age = FloatField()  # 吧龄
    register_time = DateTimeField()  # 注册时间s
    attention_field = StringField()  # 能力圈
    attention_field_url = URLField()
    abstract = StringField()
    visit_count = IntField()
    # stock_focused_on = ListField()
    his_stock_count = IntField()
    person_he_care_count = IntField()
    fans_count = IntField()
    person_he_care = ListField()
    his_stock = ListField()
    meta = {
        "indexes": [
            "publish_user_id",
            "publish_user_href"
        ],
        "unique": True
    }


if __name__ == '__main__':
    pass

