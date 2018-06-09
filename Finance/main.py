from scrapy.cmdline import execute


execute('scrapy crawl DFCFW_news'.split(' '))
# execute('scrapy crawl eastmoney -s JOBDIR=crawls/eastmoney-1'.split(' '))