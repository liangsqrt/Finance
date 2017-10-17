# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.loader import ItemLoader
import re
import requests
import json
from Finance.items import forumdata
from Finance.items import forumhtmlpage
from Finance.items import DFCFWpublisher
import datetime
import time











class CrawlSpider(CrawlSpider):
    name = 'eastmoney'
    allowed_domains = ['eastmoney.com']
    # start_urls = ['http://www.eastmoney.com/','http://guba.eastmoney.com/default,{},f_1.html.html'.format(str(i) for i in range(2,527207))]
    start_urls = ['http://guba.eastmoney.com/default_{}.html'.format(str(i)) for i in range(1,527207)]


    rules = (
        Rule(LinkExtractor(allow=r'.*?eastmoney.com/list\,.*'), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow='http://guba.eastmoney.com/news\,\d{6}\,\d{8,10}[_\d]\.html'),callback='deal_page_contain_content',follow=True),
        Rule(LinkExtractor(allow='http://guba.eastmoney.com/default_\d*.html'),callback='parse_item',follow=True),
        # Rule(LinkExtractor(allow='http://guba.eastmoney.com/news\,\S{3,7}\,\d{8,10}[_\d]\.html'),callback='parse_item',follow=True),
        # Rule(LinkExtractor(allow='default,\d*,f_1.html'), callback='parse_item', follow=True),
    )
    domians='http://guba.eastmoney.com/'
    headers={
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding':'gzip, deflate',
        'Accept-Language':'zh-CN,zh;q=0.8',
        'Host':'guba.eastmoney.com',
        'Proxy-Connection':'closed',
        'Connection':'closed'
    }

    def parse_item(self, response):
        i = {}
        print '抓取到了一个list页面'
        print response.status
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        return i








    def deal_page_contain_content(self,response):


        first_page_html={
            'mainurl':response.url,
            'datetime':datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'timestrimp':time.time(),
            'content':{
                response.url:response.body

            }
        }

        reply_data_this_page=[]
        reply_huifuuid_this_page=[]#根据这两个列表来获得点赞数
        reply_huifuid_this_page=[]

        content_list_raw= response.xpath('//div[@class="zwcontentmain"]//text()').extract()
        content_result=''
        for content_inside in content_list_raw:
            # print content_inside.strip()
            content_result+=content_inside.strip()#主贴的内容
        try:
            topicid=response.xpath('//head').re(r'var topicid="(\d*)"')[0]
        except Exception as e:
            print e
            return
        stockcode=response.xpath('//head').re(r'var code \= \"(\d*)\"\;')[0]
        other_info=response.xpath('//head/script').extract()[0]
        view_comments_num=response.xpath('//body').re(r'\{var num\=(\d*); }var pinglun_num\=(\d*)\;')
        view_num=view_comments_num[0]
        comment_num=view_comments_num[1]

        publish_user_info_div=response.xpath('//div[@id="zwcontent"]/div[@id="zwcontt"]')[0]
        publish_user_href=publish_user_info_div.xpath('//div[@id="zwconttb"]/div[@id="zwconttbn"]/strong/a/@href').extract()[0]
        publish_user_name=publish_user_info_div.xpath('//div[@id="zwconttb"]/div[@id="zwconttbn"]/strong/a/text()').extract()[0]
        publish_time=publish_user_info_div.xpath('//div[@class="zwfbtime"]/text()').re('(\d{4}\-\d{1,2}\-\d{1,2} \d{1,2}:\d{1,2}:\d{1,2})')[0]

        publish_user_item=DFCFWpublisher()
        publish_user_item['publish_user_href']=publish_user_href
        publish_user_item['publish_user_name']=publish_user_name
        yield publish_user_item


        first_page_html['publish_time']=publish_time

        try:
            data_proper=publish_user_info_div.re(r'data-popper="(\d*)"')[0]
        except :
            data_proper=0

        reply_list_div=response.xpath('//div[@id="zwlist"]/div[@class="zwli clearfix"]')
        # reply_list_div=response.css('#zwlist > div.zwli.clearfix')
        for num,one_reply in enumerate(reply_list_div):
            try:
                test_div=one_reply.extract()
                reply_id= one_reply.re(r'id="(zwli\d*)"')[0]#id

                try:
                    reply_content= one_reply.xpath('.//div[@class="zwlitext stockcodec"]/text()').extract()[0]#content[num]
                except:
                    reply_content=''#因为这里边的回复可能是空的，别人直接回复的就是一个表情图片。
                reply_publish_time= one_reply.xpath('.//div[@class="zwlitx"]/div[@class="zwlitxt"]/div[@class="zwlitime"]/text()').extract()[0]#publish_time
                reply_publish_user= one_reply.xpath('.//div[@class="zwlitx"]/div[@class="zwlitxt"]/div[@class="zwlianame"]/span[@class="zwnick"]/a[@href]/text()').extract()[0]#publish_user[num]
                reply_publish_user_href= one_reply.xpath('.//div[@class="zwlitx"]/div[@class="zwlitxt"]/div[@class="zwlianame"]/span[@class="zwnick"]/a/@href').extract()[0]#publish_user_href[num]

                reply_publish_user_photo= one_reply.xpath('.//div[@class="zwliimg"]/a[@href]/img/@src').extract()[0]#publish_user_photo[num]
                reply_data_huifuid= one_reply.re(r'data-huifuid="(\d*)"')[0]
                reply_data_huifuuid= one_reply.re(r'data-huifuuid="(\d*)"')[0]
                this_reply_info={
                    'id':reply_id,
                    'content':reply_content,
                    'publish_time':reply_publish_time,
                    'publish_user':reply_publish_user,
                    'publish_user_href':reply_publish_user_href,
                    'publish_user_photo':reply_publish_user_photo,
                    'data_huifuid':reply_data_huifuid,
                    'data_huifuuid':reply_data_huifuuid
                }
                reply_data_this_page.append(this_reply_info)
                reply_huifuid_this_page.append(reply_data_huifuid)
                reply_huifuuid_this_page.append(reply_data_huifuuid)

                publish_user_item = DFCFWpublisher()
                publish_user_item['publish_user_href'] = reply_publish_user_href
                publish_user_item['publish_user_name'] = reply_publish_user
                yield publish_user_item


            except Exception as e:
                print e
        #再次统计点赞数也可以将来根据数据库中的缓存舒俱来更新，也可以在这里就更新


        url_dianzan='http://iguba.eastmoney.com/interf/guba.aspx?&action=getreplylikegd&id='+topicid+'&replyids='
        if reply_huifuid_this_page:
            for num,comment_id in enumerate(reply_huifuid_this_page):
                url_dianzan+='%2C'+comment_id+'%7C'+reply_huifuuid_this_page[num]
            url_dianzan=url_dianzan+'&code='+str(stockcode)
            try:
                dianzan_info_response=requests.get(url=url_dianzan,timeout=5)
                dianzan_info_response_text=dianzan_info_response.text.lstrip('(').rstrip(')')
                dianzhan_data_json=json.loads(dianzan_info_response_text)
                for num,count_info in enumerate(dianzhan_data_json['result']):
                    reply_data_this_page[num]['like_count']=count_info['count']
            except Exception as e:
                print e


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
                    'content':content_result,
                    'topicid':topicid,
                    'publish_user':publish_user_name,
                    'publish_user_href':publish_user_href,
                    'publish_time':publish_time,
                    'reply_nodes':reply_data_this_page,
                    'data_proper':data_proper,
                    'url':response.url,
                    'read_count':view_num,
                    'reply_count':comment_num,
                    'stockcode':stockcode,
                    'other_info':other_info,
                    'html_page':first_page_html

                }
                yield scrapy.Request(url=nex_page_url,callback=self.deal_page_contain_content_fallow,method='get',headers=self.headers,meta=the_data_send_to_meta)


                publish_user_item = DFCFWpublisher()
                publish_user_item['publish_user_href'] = publish_user_href
                publish_user_item['publish_user_name'] = publish_user_name
                yield publish_user_item



            else:
                thisitem = forumdata()
                thisitem['content'] = content_result
                thisitem['topicid'] = topicid
                thisitem['publish_user'] = publish_user_name
                thisitem['publish_user_href'] = publish_user_href
                thisitem['publish_time'] = publish_time
                thisitem['reply_nodes'] = reply_data_this_page
                thisitem['data_proper'] = data_proper
                thisitem['url']=response.url
                thisitem['read_count']=view_num
                thisitem['reply_count']=comment_num
                thisitem['stockcode']=stockcode
                thisitem['other_info']=other_info
                yield thisitem



                publish_user_item = DFCFWpublisher()
                publish_user_item['publish_user_href'] = publish_user_href
                publish_user_item['publish_user_name'] = publish_user_name
                yield publish_user_item



                firstpage_item=forumhtmlpage()
                firstpage_item['mainurl']=response.url
                firstpage_item['datetime']=first_page_html['datetime']
                firstpage_item['timestrimp']=first_page_html['timestrimp']
                firstpage_item['content']=first_page_html['content']
                firstpage_item['publish_time']=first_page_html['publish_time']
                yield firstpage_item

        else:
            thisitem=forumdata()
            thisitem['content']=content_result
            thisitem['topicid']=topicid
            thisitem['publish_user']=publish_user_name
            thisitem['publish_user_href']=publish_user_href
            thisitem['publish_time']=publish_time
            thisitem['reply_nodes']=reply_data_this_page
            thisitem['data_proper']=data_proper
            thisitem['url']=response.url
            thisitem['read_count'] = view_num
            thisitem['reply_count'] = comment_num
            thisitem['stockcode']=stockcode
            thisitem['other_info']=other_info
            yield thisitem

            firstpage_item = forumhtmlpage()
            firstpage_item['mainurl'] = response.url
            firstpage_item['datetime'] = first_page_html['datetime']
            firstpage_item['timestrimp'] = first_page_html['timestrimp']
            firstpage_item['content'] = first_page_html['content']
            firstpage_item['publish_time']=first_page_html['publish_time']
            yield firstpage_item


            publish_user_item = DFCFWpublisher()
            publish_user_item['publish_user_href'] = publish_user_href
            publish_user_item['publish_user_name'] = publish_user_name
            yield publish_user_item

        pass







    def deal_page_contain_content_fallow(self,response):
        reply_data_this_page=[]
        reply_huifuuid_this_page=[]#根据这两个列表来获得点赞数
        reply_huifuid_this_page=[]

        fallow_page_html={
            response.url:response.body
        }



        reply_list_div = response.xpath('//div[@id="zwlist"]/div[@class="zwli clearfix"]')
        for num, one_reply in enumerate(reply_list_div):
            try:
                reply_id = one_reply.re(r'id="(zwli\d*)"')[0]  # id
                try:
                    reply_content = one_reply.xpath('.//div[@class="zwlitext stockcodec"]/text()').extract()[0]  # content
                except:
                    reply_content=''
                reply_publish_time = one_reply.xpath('.//div[@class="zwlitime"]/text()').extract()[0]  # publish_time
                reply_publish_user = \
                one_reply.xpath('.//div[@class="zwlianame"]/span[@class="zwnick"]/a[@href]/text()').extract()[
                    0]  # publish_user
                reply_publish_user_href = \
                one_reply.xpath('.//div[@class="zwlianame"]/span[@class="zwnick"]/a/@href').extract()[
                    0]  # publish_user_href

                reply_publish_user_photo = one_reply.xpath('.//div[@class="zwliimg"]/a[@href]/img/@src').extract()[
                    0]  # publish_user_photo
                reply_data_huifuid = one_reply.re(r'data-huifuid="(\d*)"')[0]
                reply_data_huifuuid = one_reply.re(r'data-huifuuid="(\d*)"')[0]
                this_reply_info = {
                    'id': reply_id,
                    'content': reply_content,
                    'publish_time': reply_publish_time,
                    'publish_user': reply_publish_user,
                    'publish_user_href': reply_publish_user_href,
                    'publish_user_photo': reply_publish_user_photo,
                    'data_huifuid': reply_data_huifuid,
                    'data_huifuuid': reply_data_huifuuid
                }
                response.meta['reply_nodes'].append(this_reply_info)
                reply_data_this_page.append(this_reply_info)
                reply_huifuid_this_page.append(reply_data_huifuid)
                reply_huifuuid_this_page.append(reply_data_huifuuid)
            except Exception as e:
                print e
        # 再次统计点赞数也可以将来根据数据库中的缓存舒俱来更新，也可以在这里就更新

        url_dianzan = 'http://iguba.eastmoney.com/interf/guba.aspx?&action=getreplylikegd&id=' + response.meta['topicid'] + '&replyids='
        if reply_huifuid_this_page:
            for num, comment_id in enumerate(reply_huifuid_this_page):
                url_dianzan += '%2C' + comment_id + '%7C' + reply_huifuuid_this_page[num]
            url_dianzan = url_dianzan + '&code=' + response.meta['stockcode']
            try:
                dianzan_info_response = requests.get(url=url_dianzan, timeout=5)
                dianzhan_data_json = json.loads(dianzan_info_response.text.lstrip('(').rstrip(')'))
                for num, count_info in enumerate(dianzhan_data_json['result']):
                    reply_data_this_page[num]['like_count'] = count_info['count']
            except Exception as e:
                print e

        next_page_div = response.xpath('//body').re(r'<div class="pager talc zwpager">[\S|\s]*?<\/div>')

        this_page_html = response.meta['html_page']
        this_page_html['content'].update(fallow_page_html)


        if next_page_div:
            Re_find_page_info = re.compile(
                r'data-page="(\S{2,6}\,\S{2,6}\,\d{6,12}\_)\|(\d{1,8})\|(\d{1,3})\|(\d{1,5})')
            next_info_find_by_re = Re_find_page_info.findall(next_page_div[0])

            page_path_of_this = next_info_find_by_re[0][0]
            total_page_num = int(next_info_find_by_re[0][1])
            page_numm_of_this = int(next_info_find_by_re[0][3])
            if page_numm_of_this <= total_page_num / 30 + 1:
                nex_page_url = self.domians + page_path_of_this + str(page_numm_of_this + 1) + '.html'
                try:
                    the_data_send_to_meta = {
                        'content': response.meta['content'],
                        'topicid': response.meta['topicid'],
                        'publish_user': response.meta['publish_user'],
                        'publish_user_href': response.meta['publish_user_href'],
                        'publish_time': response.meta['publish_time'],
                        'reply_nodes': response.meta['reply_nodes'],
                        'data_proper': response.meta['data_proper'],
                        'url':response.meta['url'],
                        'read_count':response.meta['read_count'],
                        'reply_count':response.meta['reply_count'],
                        'other_info':response.meta['other_info'],
                        'stockcode':response.meta['stockcode'],
                        'html_page':this_page_html

                    }
                except Exception as e:
                    print e

                yield scrapy.Request(url=nex_page_url, callback=self.deal_page_contain_content_fallow, method='get',
                                     headers=self.headers, meta=the_data_send_to_meta)
            else:
                thisitem = forumdata()
                thisitem['content'] = response.meta['content']
                thisitem['topicid'] = response.meta['topicid']
                thisitem['publish_user'] = response.meta['publish_user']
                thisitem['publish_user_href'] = response.meta['publish_user_href']
                thisitem['publish_time'] = response.meta['publish_time']
                thisitem['reply_nodes'] = response.meta['reply_nodes']
                thisitem['data_proper'] = response.meta['data_proper']
                thisitem['read_count']=response.meta['read_count']
                thisitem['reply_count']=response.meta['reply_count']
                thisitem['url']=response.meta['url']
                thisitem['stockcode']=response.meta['stockcode']
                thisitem['other_info']=response.meta['other_info']
                yield thisitem


                fallowpage_item=forumhtmlpage()
                fallowpage_item['mainurl']=this_page_html['mainurl']
                fallowpage_item['datetime']=this_page_html['datetime']
                fallowpage_item['timestrimp']=this_page_html['timestrimp']
                fallowpage_item['content']=this_page_html['content']
                fallowpage_item['publish_time']=this_page_html['publish_time']
                yield fallowpage_item

        else:
            thisitem = forumdata()
            thisitem['content'] = response.meta['content']
            thisitem['topicid'] = response.meta['topicid']
            thisitem['publish_user'] = response.meta['publish_user']
            thisitem['publish_user_href'] = response.meta['publish_user_href']
            thisitem['publish_time'] = response.meta['publish_time']
            thisitem['reply_nodes'] = response.meta['reply_nodes']
            thisitem['data_proper'] = response.meta['data_proper']
            thisitem['read_count'] = response.meta['read_count']
            thisitem['reply_count'] = response.meta['reply_count']
            thisitem['url']=response.meta['url']
            thisitem['stockcode']=response.meta['stockcode']
            thisitem['other_info']=response.meta['other_info']
            yield thisitem

            fallowpage_item = forumhtmlpage()
            fallowpage_item['mainurl'] = this_page_html['mainurl']
            fallowpage_item['datetime'] = this_page_html['datetime']
            fallowpage_item['timestrimp'] = this_page_html['timestrimp']
            fallowpage_item['content'] = this_page_html['content']
            fallowpage_item['publish_time']=this_page_html['publish_time']
            yield fallowpage_item
