#_*_coding:utf-8_*_
import scrapy
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider
from Finance.items import forumhtmlpage
from scrapy.loader import ItemLoader
import datetime
import time
import re
from w3lib.url import urlencode,urljoin
from scrapy.loader.processors import MapCompose
from scrapy.loader.processors import TakeFirst
from scrapy.exceptions import CloseSpider


class pagespider(CrawlSpider):
    name = 'pagespider'
    allowed_domains = ['eastmoney.com']
    start_urls = ['http://guba.eastmoney.com/default_{}.html'.format(str(i)) for i in range(21000,527207)]

    headers={
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding':'gzip, deflate',
        'Accept-Language':'zh-CN,zh;q=0.8',
        'Host':'guba.eastmoney.com',
        'Proxy-Connection':'closed',
        'Connection':'closed'
    }
    domians='http://guba.eastmoney.com/'


    rules = (
        Rule(LinkExtractor(allow=r'.*?eastmoney.com/list\,.*'), callback='parse', follow=True),  # True该False
        Rule(LinkExtractor(allow='http://guba.eastmoney.com/news\,\d{6}\,\d{8,10}\.html'),
             callback='savePageInfo', follow=False),  # True该False
        Rule(LinkExtractor(allow='news\,\d{6}\,\d{8,10}\.html'),
             callback='savePageInfo', follow=False,process_links=lambda x:'http://guba.eastmoney.com/'+x),  # True该False
        # Rule(LinkExtractor(allow='http://guba.eastmoney.com/default_\d*.html'),callback='parse_item',follow=False),#True改False
        # Rule(LinkExtractor(allow='http://guba.eastmoney.com/news\,\S{3,7}\,\d{8,10}[_\d]\.html'),callback='parse_item',follow=True),
        # Rule(LinkExtractor(allow='default,\d*,f_1.html'), callback='parse_item', follow=True),
    )

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url,headers=self.headers)


    def parse(self, response):
        print ('抓取到了一个评论list页面')
        raise CloseSpider(response.url)

        urls_list=response.selector.re(r'(news\,\d{6}\,\d{8,10}\.html)')
        for url_detail in urls_list:
            url_detail2=urljoin(self.domians,url_detail)
            yield scrapy.Request(url=url_detail2,headers=self.headers,callback=self.savePageInfo)





    def savePageInfo(self,response):

        def deal_time(time):
            Re_find_time=re.compile(r'(\d{4}\-\d{2}\-\d{2} \d{2}:\d{2}:\d{2})')
            time_str=Re_find_time.findall(time)
            return str(time_str)


        print ('in savepageinfo')
        loader1=ItemLoader(item=forumhtmlpage(),response=response)
        loader1.default_output_processor=TakeFirst()
        loader1.add_value('mainurl',response.url)
        loader1.add_value('timestrimp',time.time()*1000)
        loader1.add_value('datetime',datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        # loader1.add_xpath('publish_time','.//div[@class="zwfbtime"]/text()',MapCompose(deal_time()))
        loader1.add_xpath('publish_time',str(int(time.time()*1000)))
        loader1.add_value('content',response.body)

        pageItem=loader1.load_item()

        next_page_div= response.xpath('//body').re(r'<div class="pager talc zwpager">[\S|\s]*?<\/div>')
        if next_page_div:
            Re_find_page_info=re.compile(r'data-page="(\S{2,6}\,\S{2,6}\,\d{6,12}\_)\|(\d{1,8})\|(\d{1,3})\|(\d{1,5})')
            next_info_find_by_re=Re_find_page_info.findall(next_page_div[0])

            page_path_of_this=next_info_find_by_re[0][0]
            total_page_num=int(next_info_find_by_re[0][1])
            page_numm_of_this=int(next_info_find_by_re[0][3])
            if page_numm_of_this <= total_page_num/30+1:
                nex_page_url=self.domians+page_path_of_this+str(page_numm_of_this+1)+'.html'
                the_data_send_to_meta={
                    'item':pageItem
                }
                yield scrapy.Request(url=nex_page_url,callback=self.savePageInfo2,method='get',headers=self.headers,meta=the_data_send_to_meta)
            else:
                yield pageItem

    def savePageInfo2(self,response):
        last_item=response.meta['item']
        loader1=ItemLoader(item=forumhtmlpage(),response=response)
        loader1.default_output_processor=TakeFirst()
        # loader1.add_value('mainurl',last_item.get('mainurl').pop())
        # loader1.add_value('timestrimp',time.time()*1000)
        # loader1.add_value('datetime',datetime.datetime.now())
        loader1.add_value('content',response.body)

        pageItem=loader1.load_item()
        last_content=last_item['content']
        if type(last_content) is type([]):
            last_content.append(pageItem['content'])
        else:
            last_content=[last_content,pageItem['content']]
        last_item['content']=last_content


        next_page_div= response.xpath('//body').re(r'<div class="pager talc zwpager">[\S|\s]*?<\/div>')
        if next_page_div:
            Re_find_page_info=re.compile(r'data-page="(\S{2,6}\,\S{2,6}\,\d{6,12}\_)\|(\d{1,8})\|(\d{1,3})\|(\d{1,5})')
            next_info_find_by_re=Re_find_page_info.findall(next_page_div[0])

            page_path_of_this=next_info_find_by_re[0][0]
            total_page_num=int(next_info_find_by_re[0][1])
            page_numm_of_this=int(next_info_find_by_re[0][3])
            if page_numm_of_this <= total_page_num/30+1:
                nex_page_url=self.domians+page_path_of_this+str(page_numm_of_this+1)+'.html'
                the_data_send_to_meta={
                    'item':last_item
                }
                yield scrapy.Request(url=nex_page_url,callback=self.savePageInfo2,method='get',headers=self.headers,meta=the_data_send_to_meta)



            else:
                yield last_item