#_*_coding:utf-8_*_
import pymongo
import time





client=pymongo.MongoClient('localhost',27017)
col=client['Finance']
db=col['DFCFW']

while True:
    client = pymongo.MongoClient('localhost', 27017)
    col = client['Finance']
    db = col['DFCFW10_4']
    print db.find().count()


    client.close()
    time.sleep(2)


# for one_item in db.find():
#     if len(one_item['reply_nodes'])>30:
#         print one_item['url']


# for i in db.find({'url':'http://guba.eastmoney.com/news,000839,689176541.html'}):
#     for j in i['reply_nodes']:
#         print '--------',j['content']