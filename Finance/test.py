from items import *
import datetime



rowhtml1 = RawHtmlMongo()
rowhtml1.board = "test1"
rowhtml1.url = "http://www.baidu.com"
rowhtml1.datetime = datetime.datetime.now()
rowhtml1.content = "test1"
rowhtml1.publish_time = datetime.datetime.now()
rowhtml1.spider_time = datetime.datetime.now()
rowhtml1.save()
