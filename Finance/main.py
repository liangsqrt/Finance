from scrapy.cmdline import execute
from Finance.settings import *
import redis


# start_urls = [
#         "http://guba.eastmoney.com/default,0_1.html",
#         "http://guba.eastmoney.com/default,99_1.html",
#     ]
#
#
# pool = redis.ConnectionPool(
#         host=REDIS_HOST, port=REDIS_PORT, db=REDIS_PARAMS["db"], password=REDIS_PARAMS["password"])
# redis = redis.Redis(connection_pool=pool)
#
# for i in start_urls:
#     redis.lpush("DFCFW_forum:start_urls", i)
execute('scrapy crawl DFCFW_forum'.split(' '))
# execute('scrapy crawl eastmoney -s JOBDIR=crawls/eastmoney-1'.split(' '))
