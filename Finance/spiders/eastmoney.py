# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.loader import ItemLoader
import re
import requests
import json
from Finance.items import forumdata

#http://gubawebapi.eastmoney.com/v3/package/getdata/common?url=read/Custom/Mobie/ArticleReplyList.aspx?id%3D20170917777800732%26sort%3D-1%26ps%3D10%26p%3D2%26type%3D1%26deviceid%3D0.3410789631307125%26version%3D100%26product%3DGuba%26plat%3DWeb&callback=jQuery18305983288689322457_1505716763206&_=1505716777964
#上边的是评论的链接








class CrawlSpider(CrawlSpider):
    name = 'eastmoney'
    allowed_domains = ['eastmoney.com']
    start_urls = ['http://www.eastmoney.com/']

    rules = (
        Rule(LinkExtractor(allow=r'.*?eastmoney.com/list\,.*'), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow='http://guba.eastmoney.com/news\,\d{6}\,\d{8,10}[_\d]\.html'),callback='deal_page_contain_content',follow=True),
        Rule(LinkExtractor(allow='http://guba.eastmoney.com/default_\d*.html'),callback='parse_item',follow=True)
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
        print response.status
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        return i
        print 'hello'







    def deal_page_contain_content(self,response):

        reply_data_this_page=[]
        reply_huifuuid_this_page=[]#根据这两个列表来获得点赞数
        reply_huifuid_this_page=[]

        content_list_raw= response.xpath('//div[@class="zwcontentmain"]//text()').extract()
        content_result=''
        for content_inside in content_list_raw:
            print content_inside.strip()
            content_result+=content_inside.strip()#主贴的内容
        topicid=response.xpath('//head').re(r'var topicid="(\d*)"')[0]
        publish_user_info_div=response.xpath('//div[@id="zwcontent"]/div[@id="zwcontt"]')[0]
        publish_user_href=publish_user_info_div.xpath('//div[@id="zwconttb"]/div[@id="zwconttbn"]/strong/a/@href').extract()[0]
        publish_user_name=publish_user_info_div.xpath('//div[@id="zwconttb"]/div[@id="zwconttbn"]/strong/a/text()').extract()[0]
        publish_time=publish_user_info_div.xpath('//div[@class="zwfbtime"]/text()').re('(\d{4}\-\d{1,2}\-\d{1,2} \d{1,2}:\d{1,2}:\d{1,2})')[0]
        try:
            data_proper=publish_user_info_div.re(r'data-popper="(\d*)"')[0]
        except :
            data_proper=0

        # reply_list_div=response.xpath('//div[@id="zwlist"]/div[@class="zwli clearfix"]')
        reply_list_div=response.css('#zwlist > div.zwli.clearfix')
        for num,one_reply in enumerate(reply_list_div):

            reply_id= one_reply.re(r'id="(zwli\d*)"')[0]#id
            reply_content= one_reply.xpath('//div[@class="zwlitext stockcodec"]/text()').extract()#content[num]
            reply_content=one_reply.css('div.zwlitext.stockcodec::text').extract()
            reply_publish_time= one_reply.xpath('//div[@class="zwlitime"]/text()').extract()[num]#publish_time
            reply_publish_user= one_reply.xpath('//div[@class="zwlianame"]/span[@class="zwnick"]/a[@href]/text()').extract()#publish_user[num]
            reply_publish_user_href= one_reply.xpath('//div[@class="zwlianame"]/span[@class="zwnick"]/a/@href').extract()#publish_user_href[num]

            reply_publish_user_photo= one_reply.xpath('//div[@class="zwliimg"]/a[@href]/img/@src').extract()#publish_user_photo[num]
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
        #再次统计点赞数也可以将来根据数据库中的缓存舒俱来更新，也可以在这里就更新

        url_dianzan='http://iguba.eastmoney.com/interf/guba.aspx?&action=getreplylikegd&id='+topicid+'&replyids='
        if reply_huifuid_this_page:
            for num,comment_id in enumerate(reply_huifuid_this_page):
                url_dianzan+='%2C'+comment_id+'%7C'+reply_huifuuid_this_page[num]
            try:
                dianzan_info_response=requests.get(url=url_dianzan,timeout=5)
                dianzhan_data_json=json.loads(dianzan_info_response.text)
                for num,count_info in dianzhan_data_json['result']:
                    reply_data_this_page[num]['like_count']=count_info['count']
            except Exception as e:
                print e

        '''
http://iguba.eastmoney.com/interf/guba.aspx?&action=getreplylikegd&id=663609789&replyids=8460705806%7C3820111804331630%2C8460713385%7C1964094426516620%2C8460761860%7C9918094338151018%2C8460762703%7C4572124780026602%2C8460765848%7C8922094107029768%2C8460768871%7C8482094305564800%2C8460773228%7C5638024574020492%2C8460775140%7C9871094289331750%2C8460780799%7C2344054547537194%2C8460782072%7C7964212886481972%2C8460785655%7C4530094278839102%2C8460788697%7C4123112789689664%2C8460790513%7C5051113920659638%2C8460791119%7C5051113920659638%2C8460791778%7C5051113920659638%2C8460792045%7C4308014805058230%2C8460796416%7C5677013774933318%2C8460797823%7C8754113241610758%2C8460797659%7C9330094297552088%2C8460801842%7C6202094159489410%2C8460806168%7C5638024574020492%2C8460810543%7C1423094308893214%2C8460815374%7C8289113948792576%2C8460817643%7C4123112789689664%2C8460824605%7C6880094005660300%2C8460825512%7C2584112005181678%2C8460832187%7C7962094345884686%2C8460838670%7C3049024933758630%2C8460839606%7C7899094659301468%2C8460847337%7C4308014805058230&code=601166        '''



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
                    'url':response.url

                }
                yield scrapy.Request(url=nex_page_url,callback=self.deal_page_contain_content_fallow,method='get',headers=self.headers,meta=the_data_send_to_meta)

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

                yield thisitem

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
            yield thisitem

        pass







    def deal_page_contain_content_fallow(self,response):
        reply_data_this_page=[]
        reply_huifuuid_this_page=[]#根据这两个列表来获得点赞数
        reply_huifuid_this_page=[]

        reply_list_div = response.xpath('//div[@id="zwlist"]/div[@class="zwli clearfix"]')
        for num, one_reply in enumerate(reply_list_div):
            reply_id = one_reply.re(r'id="(zwli\d*)"')[0]  # id
            reply_content = one_reply.xpath('//div[@class="zwlitext stockcodec"]/text()').extract()[num]  # content
            reply_publish_time = one_reply.xpath('//div[@class="zwlitime"]/text()').extract()[num]  # publish_time
            reply_publish_user = \
            one_reply.xpath('//div[@class="zwlianame"]/span[@class="zwnick"]/a[@href]/text()').extract()[
                num]  # publish_user
            reply_publish_user_href = \
            one_reply.xpath('//div[@class="zwlianame"]/span[@class="zwnick"]/a/@href').extract()[
                num]  # publish_user_href

            reply_publish_user_photo = one_reply.xpath('//div[@class="zwliimg"]/a[@href]/img/@src').extract()[
                num]  # publish_user_photo
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
        # 再次统计点赞数也可以将来根据数据库中的缓存舒俱来更新，也可以在这里就更新

        url_dianzan = 'http://iguba.eastmoney.com/interf/guba.aspx?&action=getreplylikegd&id=' + response.meta['topicid'] + '&replyids='
        if reply_huifuid_this_page:
            for num, comment_id in enumerate(reply_huifuid_this_page):
                url_dianzan += '%2C' + comment_id + '%7C' + reply_huifuuid_this_page[num]
            try:
                dianzan_info_response = requests.get(url=url_dianzan, timeout=5)
                dianzhan_data_json = json.loads(dianzan_info_response.text)
                for num, count_info in dianzhan_data_json['result']:
                    reply_data_this_page[num]['like_count'] = count_info['count']
            except Exception as e:
                print e

        next_page_div = response.xpath('//body').re(r'<div class="pager talc zwpager">[\S|\s]*?<\/div>')
        if next_page_div:
            Re_find_page_info = re.compile(
                r'data-page="(\S{2,6}\,\S{2,6}\,\d{6,12}\_)\|(\d{1,8})\|(\d{1,3})\|(\d{1,5})')
            next_info_find_by_re = Re_find_page_info.findall(next_page_div[0])

            page_path_of_this = next_info_find_by_re[0][0]
            total_page_num = int(next_info_find_by_re[0][1])
            page_numm_of_this = int(next_info_find_by_re[0][3])
            if page_numm_of_this <= total_page_num / 30 + 1:
                nex_page_url = self.domians + page_path_of_this + str(page_numm_of_this + 1) + '.html'

                the_data_send_to_meta = {
                    'content': response.meta['content'],
                    'topicid': response.meta['topicid'],
                    'publish_user': response.meta['publish_user'],
                    'publish_user_href': response.meta['publish_user_href'],
                    'publish_time': response.meta['publish_time'],
                    'reply_nodes': response.meta['reply_nodes'],
                    'data_proper': response.meta['data_proper'],
                    'url':response.meta['url']

                }

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
                thisitem['url']=response.meta['url']
                yield thisitem
        else:
            thisitem = forumdata()
            thisitem['content'] = response.meta['content']
            thisitem['topicid'] = response.meta['topicid']
            thisitem['publish_user'] = response.meta['publish_user']
            thisitem['publish_user_href'] = response.meta['publish_user_href']
            thisitem['publish_time'] = response.meta['publish_time']
            thisitem['reply_nodes'] = response.meta['reply_nodes']
            thisitem['data_proper'] = response.meta['data_proper']
            thisitem['url']=response.meta['url']
            yield thisitem