from scrapy.cmdline import execute


# execute('scrapy crawl eastmoney'.split(' '))
# execute('scrapy crawl eastmoney -s JOBDIR=crawls/eastmoney-1'.split(' '))
execute('scrapy crawl pagespider'.split(' '))