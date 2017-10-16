#_*_coding:utf-8_*_
import requests
import socket
import json
import time
import random
import sys
import threading
import redis


class proxy_server:
    def __init__(self):
        self.pool1 = redis.ConnectionPool(host='localhost', port=6379)
        self.redis1 = redis.Redis(connection_pool=self.pool1)
        self.url = 'http://svip.kuaidaili.com/api/getproxy/?orderid=953994536123042&num=100&b_pcchrome=1&b_pcie=1&b_pcff=1&protocol=1&method=1&an_an=1&an_ha=1&sp1=1&quality=2&sort=1&format=json&sep=1'
        self.proxy_list = []
        self.examing_url = 'http://www.eastmoney.com/'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Connection': 'close'
        }
        self.proxy_list_name='proxy_dict_list'

    def get_proxy_from_web(self):
        response1=requests.get(self.url)
        proxy_data=json.loads(response1.text)
        proxy_list= proxy_data['data']['proxy_list']
        return proxy_list


    def examing_proxy(self,proxy_list):
        for i in proxy_list:
            try:
                timea = time.time()
                proxy_raw={
                    'http':'http://'+str(i),
                    'https':'http://'+str(i)
                }
                __nouse=requests.get(url=self.examing_url,proxies=proxy_raw,timeout=10)
                timeb=time.time()
                timeused=timeb-timea
                if timeused<3:
                    proxy_good_dict={
                        'used_times':0,
                        'proxy':i
                    }
                    if self.redis1.llen(self.proxy_list_name)<500:
                        self.redis1.lpush(self.proxy_list_name,proxy_good_dict)
                else:
                    pass
            except Exception as e:
                print e


    def run(self):
        while True:
            proxy_list=self.get_proxy_from_web()
            self.examing_proxy(proxy_list)


    def get_proxy(self):
        proxy=self.redis1.rpop(self.proxy_list_name)
        while True:
            if proxy['used_times']<100:
                proxy['used_times']+=1
                self.redis1.lpush(self.proxy_list_name,proxy)
                return proxy['proxy']
            else:
                pass



if __name__ == '__main__':
    thisclass=proxy_server()
    thisclass.run()