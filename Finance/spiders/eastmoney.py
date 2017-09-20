# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.loader import ItemLoader



#http://gubawebapi.eastmoney.com/v3/package/getdata/common?url=read/Custom/Mobie/ArticleReplyList.aspx?id%3D20170917777800732%26sort%3D-1%26ps%3D10%26p%3D2%26type%3D1%26deviceid%3D0.3410789631307125%26version%3D100%26product%3DGuba%26plat%3DWeb&callback=jQuery18305983288689322457_1505716763206&_=1505716777964
#上边的是评论的链接








class CrawlSpider(CrawlSpider):
    name = 'eastmoney'
    allowed_domains = ['eastmoney.com']
    start_urls = ['http://www.eastmoney.com/']

    rules = (
        Rule(LinkExtractor(allow=r'.*?eastmoney.com/list\,.*'), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow='http://guba.eastmoney.com/news\,\d{6}\,\d{8,10}[_\d]\.html'),callback='deal_page_contain_content',follow=True)
    )

    def parse_item(self, response):
        i = {}
        print response.status
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        return i
        print 'hello'


    def deal_page_contain_content(self,response):
        pass
        content_list_raw= response.xpath('//div[@class="zwcontentmain"]//text()').extract()
        content_result=''
        for content_inside in content_list_raw:
            print content_inside.strip()
            content_result+=content_inside.strip()
        reply_list_div=response.xpath('//div[@id="zwlist"]/div[@class="zwli clearfix"]')
        for one_reply in reply_list_div:
            # print one_reply.css('div[id]').get('id')
            # print one_reply.css('div').get('id').extract()
            # print one_reply.xpath('div::id')
            print one_reply.re(r'id="(zwli\d*)"')[0]
            print one_reply.xpath('//div[@class="zwlitx"]//div[@class="zwlitext stockcodec"]/text()').extract()[0]#content
            print one_reply.xpath('//div[@class="zwlitx"]//div[@class="zwlitime"]/text()').extract()[0]#publish_time
            for i in one_reply.xpath('//div[@class="zwlitx"]//div[@class="zwlianame"]/span[@class="zwnick"]/a[@href]/text()').extract():#publish_user
                print i
            print one_reply.xpath('//div[@class="zwlitx"]//div[@class="zwlianame"]/span[@class="zwnick"]/a/@href').extract()[0]#publish_user_href

            print one_reply.xpath('//div[@class="zwliimg"]/a[@href]/img/@src').extract()
        pass
