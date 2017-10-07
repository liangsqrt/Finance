import pymongo
import redis




rconnect_pool=redis.ConnectionPool(host='localhost',port=6379,db=0)
rclient=redis.Redis(connection_pool=rconnect_pool)


mongoclient=pymongo.MongoClient('localhost',27017)
mongoCOL=mongoclient['Finance']
mongoDB=mongoCOL['DFCFW10_4']


print mongoDB.find().count()
for i in mongoDB.find({},{'publish_user_href':1,'reply_nodes':1}):
    # print i['publish_user_href']
    rclient.sadd('publish_user_href',i['publish_user_href'])
    for reply_node_info in i['reply_nodes']:
        rclient.sadd('publish_user_href',reply_node_info['publish_user_href'])