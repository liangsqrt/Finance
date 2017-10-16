# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
import redis
import json

redis_connection_pool=redis.ConnectionPool(host='localhost', port=6379)
redis1 = redis.Redis(connection_pool=redis_connection_pool)
redis_proxy_list_name='proxy_dict_list'



class FinanceSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class HttpProxyMiddleware(object):
    def process_request(self,request,spider):
        while True:
            try:
                proxy_dict_raw=redis1.rpop(redis_proxy_list_name)
                if not proxy_dict_raw:
                    break
                else:
                    proxy_dict=json.loads(proxy_dict_raw)
                if proxy_dict['used_times']<300:
                    proxy=proxy_dict['proxy']
                    proxy_dict['used_times']+=1
                    proxy_dict_json=json.dumps(proxy_dict)
                    redis1.lpush(redis_proxy_list_name,proxy_dict_json)
                    proxy = 'http://' + proxy
                    request.meta['proxy'] = proxy
                    break
                else:
                    pass
            except Exception as e:
                print e
            finally:
                break