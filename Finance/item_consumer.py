#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/4 0004 16:27
# @Author  : LiangLiang
# @Site    : 
# @File    : item_consumer.py
# @Software: PyCharm
from scrapy.utils.project import get_project_settings
get_project_settings()
from Finance.pipelines import *
from Finance.items import *
from sqlalchemy.engine import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy import and_
import redis
import time
from flask import Flask, Response
from prometheus_client import Gauge,Counter
import threading
import pickle
from Finance.spiders.DFCFW_forum import DFCFW_news
import prometheus_client
from prometheus_client.core import CollectorRegistry



connect('东方财富网', host="192.168.31.107", port=27017)

app = Flask("item_comsuer")

registry1 = CollectorRegistry()

try:
    gauge = Gauge(name="consumer_gauge_info",
                  documentation="外网服务器消费者运行监控",
                  labelnames=["trade_type", "trade_code", "data_type"], registry=registry1)
except Exception as e:
    print(e)

try:
    counter = Counter(name="consumer_counter_info",
                      documentation="外网服务器消费者运行监控",
                      labelnames=["trade_type","trade_code", "data_type"], registry=registry1)
except Exception as e:
    print(e)


@app.route('/status')
def status():
    return


@app.route("/metrics")
def comsumer_status():
    return Response(prometheus_client.generate_latest(registry1), mimetype="text/plain")


class VirtualSpider(object):
    """
    满足pipeline的构造
    """
    def __init__(self):
        name = "closespider_id"
        session = None


class SQLConsumer(object):
    def __init__(self):
        self.settings = get_project_settings()
        self.sql_host = self.settings.get("SQL_HOST")
        self.sql_port = self.settings.get("SQL_PORT")
        self.sql_db = self.settings.get("SQL_DB")
        self.sql_user = self.settings.get("SQL_USER")
        self.sql_passwd = self.settings.get("SQL_PASSWD")
        self.sql_char = self.settings.get("SQL_CHAR")
        self.redis_host = self.settings.get("REDIS_HOST")
        self.redis_port = self.settings.get("REDIS_PORT")
        self.redis_db = self.settings.get("REDIS_DB")

        self.engine = create_engine("mysql+pymysql://{name}:{passwd}@{host}:{port}/{sql_db}?charset={charset}".format(
            name=self.sql_user, passwd=self.sql_passwd, host=self.sql_host, port=self.sql_port,
            sql_db=self.sql_db, charset=self.sql_char
        ))
        self.session = sessionmaker(bind=self.engine)()
        self.pool = redis.ConnectionPool(host=self.redis_host, port=self.redis_port, db=self.redis_db)
        self.redis = redis.Redis(connection_pool=self.pool)
        self.thread_count = self.settings.get("COMSUMER_THREAD_COUNT")

    def run(self):
        """
        通过多线程启动消费者
        :return:
        """
        thread = threading.Thread(target=self.eject_mysql_loader, args=())
        thread.start()

    def eject_mysql_loader(self):
        while True:
            threads_list =[]
            for i in threads_list:
                if not i.is_alive():
                    threads_list.remove(i)
            while len(threads_list) < self.thread_count:
                thred1 = threading.Thread(target=self.push_data_to_mysql, args=())
                thred1.start()
                threads_list.append(thred1)
            time.sleep(1)

    def push_data_to_mysql(self):
        """
        启动之后持续监控redis数据库，持续运行。
        :param host:
        :param port:
        :param db:
        :param user:
        :param passwd:
        :return:
        """
        # pipeline_jzzr = JZZRScElectricTradeSqlPipeline()
        # pipeline_fsch = FSCHScElectricTradeSqlPipeline()
        # pipeline_gpjy = GPJYScElectricTradeSqlPipeline()
        session = sessionmaker(bind=self.engine)()
        while True:
            item = self.redis.lpop("all_data")
            if not item:
                time.sleep(1)
                gauge.labels("wait", "wait", "wait").set(1)
                continue
            gauge.labels("wait", "wait", "wait").set(0)
            item = pickle.loads(item)
            spider_name = item["spider_name"]
            if spider_name == SiChuanFSCH.name:
                try:
                    spider_fsch = VirtualSpider()
                    spider_fsch.name = SiChuanFSCH.name
                    spider_fsch.session = session
                    pipeline_fsch.process_item(item, spider_fsch)
                    counter.labels(spider_name, item["trade_id"], item["data_type"]).inc()
                except Exception as e:
                    print(e)

            elif spider_name == SiChuanJZZR.name:
                try:
                    spider_jzzr = VirtualSpider
                    spider_jzzr.name = SiChuanJZZR.name
                    spider_jzzr.sessoon = session
                    pipeline_jzzr.process_item(item, spider_jzzr)
                    counter.labels(spider_name, item["trade_id"], item["data_type"]).inc()
                except Exception as e:
                    print(e)
            elif spider_name == SiChuanGPJY.name:
                try:
                    spider_gpjy = VirtualSpider()
                    spider_gpjy.name = SiChuanGPJY.name
                    spider_gpjy.session = session
                    pipeline_gpjy.process_item(item, spider_gpjy)
                    counter.labels(spider_name, item["trade_id"], item["data_type"]).inc()
                except Exception as e:
                    print(e)


class MongoConsumer(object):
    def __init__(self):
        self.settings = get_project_settings()
        self.MONGO_HOST = self.settings.get("MONGO_HOST")
        self.MONGO_PORT = self.settings.get("MONGO_PORT")
        self.MONGO_DB = self.settings.get("MONGO_DB")

        self.redis_host = self.settings.get("REDIS_HOST")
        self.redis_port = self.settings.get("REDIS_PORT")
        self.redis_db = self.settings.get("REDIS_PARAMS")["db"]
        self.redis_passwd = self.settings.get("REDIS_PARAMS")["password"]

        self.pool = redis.ConnectionPool(
            host=self.redis_host, port=self.redis_port, db=self.redis_db, password=self.redis_passwd)
        self.redis = redis.Redis(connection_pool=self.pool)
        self.thread_count = self.settings.get("COMSUMER_THREAD_COUNT")

    def run(self):
        """
        通过多线程启动消费者
        :return:
        """
        thread = threading.Thread(target=self.eject_mongo_loader, args=())
        thread.start()

    def eject_mongo_loader(self):
        threads_list = []
        while True:
            for i in threads_list:
                if not i.is_alive():
                    threads_list.remove(i)
            while len(threads_list) < self.thread_count:
                thred1 = threading.Thread(target=self.push_data_to_mongo, args=())
                thred1.start()
                threads_list.append(thred1)
            time.sleep(1)

    def push_data_to_mongo(self):
        save_data_to_mongo_pipeline = SaveDataByMongo()
        virtual_spider = VirtualSpider()
        while True:
            item = self.redis.lpop("all_data")
            if not item:
                time.sleep(1)
                gauge.labels("wait", "wait", "wait").set(1)
                continue
            gauge.labels("wait", "wait", "wait").set(0)
            item = pickle.loads(item)
            try:
                print("si saving")
                save_data_to_mongo_pipeline.process_item(item, virtual_spider)
                print("saving down")
                print("saving down")
            except Exception as e:
                print(e)




if __name__ == '__main__':
    app.sqlcomsumenr = MongoConsumer()
    app.sqlcomsumenr.run()
    app.run(host="0.0.0.0",port=6802)


