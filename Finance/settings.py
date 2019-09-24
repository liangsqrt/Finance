# -*- coding: utf-8 -*-

# Scrapy settings for Finance project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'Finance'

SPIDER_MODULES = ['Finance.spiders']
NEWSPIDER_MODULE = 'Finance.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'Finance (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 64

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  # 'Accept-Language': 'en',
   'accept-language': 'zh-CN,zh;q=0.8',
   'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'Finance.middlewares.FinanceProxySaveMiddleware': 300,
# }

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    # 'Finance.middlewares.MyCustomDownloaderMiddleware': 543,
#    'Finance.middlewares.add_proxy_middleware': 542,
# }

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   # 'Finance.pipelines.DFCFWPipeline': 301,
   # 'scrapy_redis.pipelines.RedisPipeline': 300,
   # 'Finance.pipelines.SaveDataByMongo': 303,
   'Finance.pipelines.SaveDataByRedis': 303,
   # 'Finance.pipelines.DFCFWFansPipeline': 302,
   # 'Finance.pipelines.DFCFWStockPipeline': 301,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'


REDIS_HOST = '127.0.0.1'
REDIS_HOST = '192.168.31.169'
REDIS_PORT = '6379'
REDIS_PARAMS = {
    'db': 0,
    'password': 'asd123456',
}


SCHEDULER="scrapy_redis.scheduler.Scheduler"
DUPEFILTER_CLASS="scrapy_redis.bloom_dupefilter.RFPDupeFilter"

# FILTER_HOST = '192.168.31.169'
# FILTER_PORT = 6379
# FILTER_DB = 4
# REDIS_PARAMS = {
#     'host': '192.168.31.169',
#     'port': 6379,
#     'password': 'asd123456',
# }
#
# SCHEDULER="scrapy_redis_bloomfilter.scheduler.Scheduler"
# SCHEDULER_PERSIST = True
# SCHEDULER_QUEUE_CLASS = 'scrapy_redis_bloomfilter.queue.SpiderPriorityQueue'
# DUPEFILTER_CLASS="scrapy_redis_bloomfilter.dupefilter.RFPDupeFilter"
BLOOMFILTER_BIT = 35 # 37对应20g左右大小。
BLOOMFILTER_HASH_NUMBER = 8



REACTOR_THREADPOOL_MAXSIZE = 100
CONCURRENT_ITEMS = 500

# REDIS_PARAMS ={
#
# }


MONGO_HOST = "192.168.31.107"
MONGO_PORT = 27017
MONGO_COL = "东方财富网"


COMSUMER_THREAD_COUNT = 2

TELNETCONSOLE_USERNAME = "liang"

TELNETCONSOLE_PASSWORD = "asd123456"

username = "liang"
password = "asd123456"
