from scrapy.spiders import Spider
from scrapy import Request
from datetime import datetime
import time
from Finance.items import forumIndexPage




class indexGet(Spider):
    name = 'indexGet'

    start_urls=['http://guba.eastmoney.com/default_{}.html'.format(str(i)) for i in range(1,27928)]
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Host': 'guba.eastmoney.com',
        'Proxy-Connection': 'closed',
        'Connection': 'closed'
    }

    def start_requests(self):
        for one_url in self.start_urls:
            yield Request(url=one_url,headers=self.headers)

    def parse(self, response):

        indexItem=forumIndexPage()
        indexItem['mainurl']=response.url
        indexItem['datetime']=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        indexItem['content']=str(response.text)
        indexItem['timestrimp']=time.time()
        return indexItem