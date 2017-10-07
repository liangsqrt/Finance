import redis





connect_pool=redis.ConnectionPool(host='localhost',port=6379,db=0)
client=redis.Redis(connection_pool=connect_pool)
# print help(client)

# print client.lpush('userid','123456')
# print client.rpop('userid')
print client.sadd('userid','123456')
return1= client.smembers('userid')
# print client.spop('userid')
print len(list(client.smembers('publish_user_href')))