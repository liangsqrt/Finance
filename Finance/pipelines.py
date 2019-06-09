# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from Finance.items import RawHtml
from Finance.other_moudle import create_filename
import pymongo
import json
import platform
import hashlib
import time
from Finance.other_moudle.pipeline_nameEN_to_nameCN import getNameCN
import os
import pickle
from Finance.items import *
from scrapy.pipelines.media import MediaPipeline
import scrapy
from scrapy.utils.misc import arg_to_iter
from twisted.internet.defer import DeferredList
import pickle
import redis


class FinancePipeline(object):
    def process_item(self, item, spider):
        return item


class SaveDataByMongo(object):
    def process_item(self, item, spider):
        try:
            mongoitem = item.__create_sqlalchemy_item__()
            mongoitem.save()
            del mongoitem
        except Exception as e:
            print(e)
        # return item
        del item


class SaveDataByRedis(object):
    def process_item(self, item, spider):
        try:
            item_dumped = pickle.dumps(item)

        except Exception as e:
            print(e)
        # return item
        del item

    def open_spider(self):
        self.pool = redis.ConnectionPool(host=, port=self.redis_port, db=self.redis_db)
        self.redis = redis.Redis(connection_pool=self.pool)
        self.thread_count = self.settings.get("COMSUMER_THREAD_COUNT")


class DFCFWFansPipeline(MediaPipeline):
    def open_spider(self, spider):
        self.headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
        }
        self.spiderinfo = self.SpiderInfo(spider)

    def get_media_requests(self, item, info):
        stock_url = item["fans"]
        yield scrapy.Request(url=stock_url, headers=self.headers, method="GET")

    def item_completed(self, results, item, info):
        del item["fans"]
        del item["person_he_care"]
        if results[0][0]:
            try:
                response = results[0][1]
                fanslist = response.xpath("//div[@class='tasidb2']//ul[@class='tasiderplist']//li/a/@href").extract()
                fanslist = [x.strip().strip("/") for x in fanslist]
                person_he_care = response.xpath("//div[@class='tasidb1']//ul[@class='tasiderplist']//li/a/@href").extract()
                person_he_care = [x.strip().strip("/") for x in person_he_care]
                item["person_he_care"] = list(set(person_he_care))
                item["fans"] = list(set(fanslist))
            except Exception as e:
                print(e)
        return item

    def process_item(self, item, spider):
        if isinstance(item, PublisherInfo):
            info = self.spiderinfo
            requests = arg_to_iter(self.get_media_requests(item, info))
            dlist = [self._process_request(r, info) for r in requests]
            dfd = DeferredList(dlist, consumeErrors=1)
            return dfd.addCallback(self.item_completed, item, info)
        else:
            return item


class DFCFWStockPipeline(MediaPipeline):
    def open_spider(self, spider):
        #  todo: 1、增加用户数量，避免被封号
        self.headers = {
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
                "Cookie": "st_si=72747346219909; qgqp_b_id=96405d9f780665ad03d6328aed2f2b57; p_origin=https%3A%2F%2Fpassport2.eastmoney.com; ct=r-R8ChPJZmqF1WY8IFIigHY1y0Ii6aG7t81fUpRbYPTI7p4ST3qEeEZ-5zm7RkU8tctDvFuEguPZAuCwsxL-krS3IrmuOXf-Nf0ErcV9dPJv-iMKqrjXSH1aVQyULlHS12K008QorQQJjzf_8F-e7lYE8vhB2RZxeejVQMSYst4; ut=FobyicMgeV60R-wNFHdtrN17mhW5wDy4v9r6x1eY-wyk7BD3Q4qOgM5u27e--2Vz5DlQpGggkVwBNjS7W_QRxA8pE2WRgcRlN8g8sWEUcydlBcAo-fAhe6GdYEiUKU5cXaxmXK2-PdtHHbpdN-C_8naI7oopKJ4voq_MnOn5BPphm0WcCMVCF-4fhE-_81Q8Mh3kZQMaelEYkTD4K_gMOSoLu3VHmAkOFttp7mo6B7n9rcivNTTCVmOPZlumS1nO06LZC4rOFN3ARQ0pk-8czrDSXaInGiWE; pi=3564345589542852%3bm3564345589542852%3breboot1%3bUfUUbcfW0RZ6JgBqknIa7iXB6V0cK%2f7MSaPoGYn%2fcbebGw3tNd47%2fCmy6Hwq8U0KzZp50dXVCdGF82VMh8b7%2ffMqfvhlF3Hx8EZt18CiRG2A%2fvELeik%2bQm0iSvIueM2EGrpUoQKEq1paU%2bSwiXvijY5Ypucm0N02TahJFsmXSkmYV0nGFhhv4LxPvb2n5v3jwX6AR0v4%3b5BztCv8%2b5Rte5R%2fTSvHFFFYy2ifsGzgiw127Fx2bEKYxS5vnCEDeZJi4Cf6RUl%2fCEIytmrzw1DUuBNwPQUymUeDbS7I3oWW02QAfsKicZc%2bdHnL%2bMRehssQK2z67KBymOm%2fXXlLdAeygTa1Do%2f1YnEtPgssyZA%3d%3d; uidal=3564345589542852reboot1; sid=137744318; vtpst=|; st_asi=delete; st_pvi=06651445649880; st_sp=2019-06-06%2005%3A01%3A55; st_inirUrl=https%3A%2F%2Fwww.baidu.com%2Flink; st_sn=14; st_psi=20190606055018370-117005300001-8560595066",
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
            }
        self.data = {
            "action": "gettastock",
            "type": "hs",
            "uid": "4162005331760506"
        }
        self.spiderinfo = self.SpiderInfo(spider)

    def get_media_requests(self, item, info):
        stock_url = item["his_stock"]
        if isinstance(item["his_stock_count"], list):  # 莫名其妙
            item["his_stock_count"] = item["his_stock_count"][0]
        self.data["uid"] = item["publish_user_id"]
        yield scrapy.FormRequest(url=stock_url, headers=self.headers, method="post", formdata=self.data)

    def item_completed(self, results, item, info):
        del item["his_stock"]
        if results[0][0]:
            response = results[0][1]
            try:
                stock_list = json.loads(response.text)
                stock_list = [x.strip().split("|")[0] for x in stock_list["data"]["stklist"].split(",")]
                item["his_stock"] = stock_list
            except Exception as e:
                print(e)
        return item

    def process_item(self, item, spider):
        if isinstance(item, PublisherInfo):
            info = self.spiderinfo
            requests = arg_to_iter(self.get_media_requests(item, info))
            dlist = [self._process_request(r, info) for r in requests]
            dfd = DeferredList(dlist, consumeErrors=1)
            return dfd.addCallback(self.item_completed, item, info)
        else:
            return item


class DFCFWPersonHeCarePipeline(MediaPipeline):
    """
    没必要，在跟fans页面的内容一模一样
    """
    def open_spider(self, spider):
        self.headers = {
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
            }
        self.spiderinfo = self.SpiderInfo(spider)

    def get_media_requests(self, item, info):
        person_her_care = item["person_he_care"]
        yield scrapy.FormRequest(url=person_her_care, headers=self.headers, method="GET")

    def item_completed(self, results, item, info):
        del item["person_he_care"]
        if results[0][0]:
            response = results[0][1]
            try:
                stock_list = json.loads(response.text)
                stock_list = [x.strip().split("|")[0] for x in stock_list["data"]["stklist"].split(",")]
                item["his_stock"] = stock_list
            except Exception as e:
                print(e)

        print(item)

    def process_item(self, item, spider):
        if isinstance(item, PublisherInfo):
            info = self.spiderinfo
            requests = arg_to_iter(self.get_media_requests(item, info))
            dlist = [self._process_request(r, info) for r in requests]
            dfd = DeferredList(dlist, consumeErrors=1)
            return dfd.addCallback(self.item_completed, item, info)
        else:
            return item



if __name__ == '__main__':
    thisclass=DFCFWPipeline()
    thisclass.add_index()