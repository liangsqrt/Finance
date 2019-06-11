import scrapy
from scrapy_redis.spiders import RedisCrawlSpider
from scrapy.spiders import CrawlSpider
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from Finance.items import RawHtml, Forum, Replay, PublisherInfo
import time
import datetime
import hashlib
import json
from copy import deepcopy


class DFCFW_news(CrawlSpider):
    name = 'DFCFW_news'

    # 这里的顺序不能改变，redis中就靠顺序来定位callback。
    rules = (
        # Rule(LinkExtractor(allow=r'http\:\/\/finance\.eastmoney\.com\/\w.+\/\d*\.html'), callback='parse_content_finance', follow=False),
        # Rule(LinkExtractor(allow=r'http\:\/\/stock\.eastmoney\.com\/news\/\d+\,\d.+\.html'), callback='parse_content_stock', follow=False),
        Rule(LinkExtractor(allow=r'http\:\/\/guba\.eastmoney\.com\/news\,\w*?\,\d.+\.html'),
             callback='parse_forum', follow=True),
        Rule(LinkExtractor(allow=r'http\:\/\/iguba\.eastmoney\.com\/\d*'),
             callback="parse_person", follow=True),
        Rule(LinkExtractor(allow=r'http\:\/\/guba\.eastmoney\.com\/.*'), follow=True),


    )
    start_urls = [
        "http://guba.eastmoney.com/default,0_1.html",
        "http://guba.eastmoney.com/default,99_1.html",
    ]


    def parse_content_finance(self,response):
        """
        没有存在的必要，每一个finance板块的文章，在guba里边，也会有一张gupa的帖子。
        :param response:
        :return:
        """

        def deal_publish_time(publish_time):
            print(publish_time)
            year_str=publish_time[0:4]
            mounth_str=publish_time[4:6]
            day_str=publish_time[6:8]

            return year_str+'-'+mounth_str+'-'+day_str+' 00:00:00'

        loader1 = ItemLoader(response=response, item=RawHtml())
        loader1.add_value('board', 'DFCFW_guba')
        loader1.add_value('url', response.url)
        loader1.add_value('datetime', datetime.datetime.now())
        loader1.add_value('content', response.text)
        loader1.add_value('spider_time', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

        item1 = loader1.load_item()
        yield item1

        loader2 = ItemLoader(response=response, item=Forum())
        topic_id = response.url.split
        loader2.add_value("url", response.url)
        loader2.add_value("stock_code", response.url.split(",")[1])
        loader2.add_value("topic_id", topic_id)
        loader2.add_xpath("publish_user_href", '//div[@id="zwconttbn"]//strong/a/@href', lambda x: x[0] if x else None)
        loader2.add_xpath("publish_user", '//div[@id="zwconttbn"]//strong/a/text()', lambda x: x[0] if x else None)
        loader2.add_xpath("user_device", response.xpath(
            '//div[@class="zwfbtime"]//text()').extract_first("").strip().split(" ")[-1])
        loader2.add_value(
            "publish_time",
            response.xpath('//div[@id="zwcontt"]//div[@class="zwfbtime"]'
                           ).re("\d{4}\-\d{2}\-\d{2} \d{2}\:\d{2}\:\d{2}")[0], deal_publish_time)
        loader2.add_xpath("content", '//div[@id="post_content"]//text()', lambda x: "".join(x))
        loader2.add_xpath("forum_age", '//div[@id="zwconttbn"]//div[@class="influence_wrap"]/@data-user_age',
                          lambda x: x[0] if x else None)
        loader2.add_xpath("influence", '//div[@id="zwconttbn"]//div[@class="influence_wrap"]/@data-user_level',
                          lambda x: float(x[0]) if x else None)
        # loader2.add_value("read_count", read_count)
        # loader2.add_value("reply_count", replay_count)
        item2 = loader2.load_item()


    def parse_content_stock(self,response):
        """
        情况和finance类似，guba的数据都覆盖了他们。
        :param response:
        :return:
        """

        def deal_publish_time(publish_time):
            print(publish_time)
            year_str = publish_time[0:4]
            mounth_str = publish_time[4:6]
            day_str = publish_time[6:8]

            return year_str+'-'+mounth_str+'-'+day_str+' 00:00:00'


        loader1=ItemLoader(response=response, item=RawHtml())
        loader1.add_value('board', 'DFCFW_stock')
        loader1.add_value('mainurl', response.url)
        loader1.add_value('timestrimp', int(time.time()*1000))
        loader1.add_value('content', response.text)
        loader1.add_value('publish_time', response.url.split(',')[-1].split('.')[0],deal_publish_time)
        loader1.add_value('spider_time', time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
        loader1.add_value('id', hashlib.md5(response.url.encode('utf-8')).digest())
        item1 = loader1.load_item()
        return item1


    def parse_forum(self,response):
        """
        处理论坛的爬虫数据
        :param response:
        :return:
        """

        def deal_publish_time(publish_time):
            dt = datetime.datetime.strptime(publish_time, "%Y-%m-%d %H:%M:%S")
            return dt

        def deal_read_count(response):
            _data = response.selector.re('var post_article = (\{.*?\})\;')
            data = _data[0]
            datajson = json.loads(data)
            stock_name = datajson["post"]["post_guba"]["stockbar_name"]
            stockbar_market = datajson["post"]["post_guba"]["stockbar_market"]
            publish_user_id = datajson["post"]["post_user"]["user_nickname"]
            user_age = datajson["post"]["post_user"]["user_age"]
            user_first_en_name = datajson["post"]["post_user"]["user_first_en_name"]
            user_influ_level = datajson["post"]["post_user"]["user_influ_level"]

            read_count = datajson["post"]["post_click_count"]
            post_forward_count = datajson["post"]["post_forward_count"]
            post_comment_count = datajson["post"]["post_comment_count"]
            post_id = datajson["post"]["post_id"]
            return read_count, post_comment_count, post_forward_count, post_id

        def deal_next_page(response):
            data_page = response.xpath('//div[@class="pager talc zwpager"]//span[@id]/@data-page').extract_first(default=None)
            if data_page:
                url, replay_count, replay_count_page, page = data_page.split("|")
                replay_count = int(replay_count)
                replay_count_page = int(replay_count_page)
                page = int(page)

                if page * replay_count_page < replay_count:  # 查看评论展示完了没有
                    domain_url = "http://guba.eastmoney.com/"
                    next_page = url + str(page+1)
                    next_page = domain_url + next_page
                    return next_page

        #  保存原始网页信息
        response_copy_headers = deepcopy(response.request.headers)
        loader1 = ItemLoader(response=response, item=RawHtml())
        loader1.add_value('board', 'DFCFW_guba')
        loader1.add_value('url', response.url)
        loader1.add_value('datetime', datetime.datetime.now())
        loader1.add_value('content', response.text)
        # loader1.add_value('publish_time', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
        loader1.add_value('spider_time', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

        item1 = loader1.load_item()
        yield item1

        #  解析此条贴吧的详细信息。
        read_count, replay_count, follow_count, topic_id = deal_read_count(response)
        loader2 = ItemLoader(response=response, item=Forum())
        loader2.add_value("url", response.url)
        loader2.add_value("stock_code", response.url.split(",")[1])
        loader2.add_value("topic_id", topic_id)
        loader2.add_xpath("publish_user_href", '//div[@id="zwconttbn"]//strong/a/@href', lambda x: x[0] if x else None)
        loader2.add_xpath("publish_user", '//div[@id="zwconttbn"]//strong/a/text()', lambda x: x[0] if x else None)
        loader2.add_value("user_device", response.xpath(
            '//div[@class="zwfbtime"]//text()').extract_first("").strip().split(" ")[-1])
        loader2.add_value(
            "publish_time",
            response.xpath('//div[@id="zwcontt"]//div[@class="zwfbtime"]'
                                           ).re("\d{4}\-\d{2}\-\d{2} \d{2}\:\d{2}\:\d{2}")[0], deal_publish_time)
        loader2.add_xpath("content", '//div[@id="post_content"]//text()', lambda x: "".join(x))
        loader2.add_xpath("forum_age", '//div[@id="zwconttbn"]//div[@class="influence_wrap"]/@data-user_age',
                          lambda x: x[0] if x else None)
        loader2.add_xpath("influence", '//div[@id="zwconttbn"]//div[@class="influence_wrap"]/@data-user_level',
                          lambda x: float(x[0]) if x else None)
        loader2.add_value("read_count", read_count)
        loader2.add_value("reply_count", replay_count)
        item2 = loader2.load_item()
        next_url = deal_next_page(response)

        item2_copy = deepcopy(item2)
        if next_url:
            yield scrapy.Request(url=next_url, headers=response_copy_headers, meta={"pre_data": {
                "item": item2_copy
            }}, callback=self.parse_forum_next)
        else:
            yield item2
        publish_user_href_next = deepcopy(item2_copy["publish_user_href"])
        yield scrapy.Request(url=publish_user_href_next, headers=response_copy_headers, callback=self.parse_person)

        for comment_div in response.xpath("//div[contains(@class, 'zwli clearfix')]"):
            reply_item = Replay()
            publish_user_info = comment_div.xpath("./div[@class='data']/@data-json").extract_first(default=None)
            if publish_user_info:
                publish_user_info = json.loads(publish_user_info)
                user_id = publish_user_info["user_id"]
                user_name = publish_user_info["user_nickname"]
                influence = publish_user_info["user_influ_level"]
                forum_age = publish_user_info["user_age"]
                user_name2 = publish_user_info["user_name"]  # 用于生成用户的主页id
                reply_item["publish_user_id"] = user_id
                reply_item["publish_user"] = user_name
                reply_item["forum_age"] = forum_age
                reply_item["influence"] = influence
            publish_user_info_href = comment_div.xpath(".//div[@class='zwliimg']//a/@href").extract_first()
            _publish_time = comment_div.xpath(".//div[@class='zwlitime']").re("\d{4}\-\d{2}\-\d{2} \d{2}\:\d{2}\:\d{2}")
            publish_time = deal_publish_time(_publish_time[0]) if _publish_time else None
            comment_id = comment_div.xpath("./@data-huifuid").extract_first()
            _content = comment_div.xpath('.//div[contains(@class, "stockcodec")]//div[@class="short_text"]//text()').extract()
            reply_to = comment_div.xpath(".//div[@class='zwlitalkbox clearfix']/div[@class='zwlitalkboxtext ']/@data-huifuid").extract_first(default=None)
            content = "".join(_content)
            reply_item["publish_user_href"] = publish_user_info_href
            reply_item["publish_time"] = publish_time
            reply_item["topic_id"] = str(topic_id)
            reply_item["replay_id"] = comment_id
            reply_item["replay_to"] = str(reply_to)
            reply_item["content"] = content
            yield reply_item

            yield scrapy.Request(url=publish_user_info_href, headers=response_copy_headers, callback=self.parse_person)


    def parse_forum_next(self, response):
        """
        处理下一页的内容，主要是评论，因为正文上一个函数就已经处理完全了。
        :param response:
        :return:
        """
        def deal_publish_time(publish_time):
            dt = datetime.datetime.strptime(publish_time, "%Y-%m-%d %H:%M:%S")
            return dt

        def deal_next_page(response):
            data_page = response.xpath('//div[@class="pager talc zwpager"]//span[@id]/@data-page').extract_first(default=None)
            if data_page:
                url, replay_count, replay_count_page, page = data_page.split("|")
                replay_count = int(replay_count)
                replay_count_page = int(replay_count_page)
                page = int(page)

                if page * replay_count_page < replay_count:  # 查看评论展示完了没有
                    domain_url = "http://guba.eastmoney.com/"
                    next_page = url + str(page+1)
                    next_page = domain_url + next_page
                    return next_page

        last_item = deepcopy(response.meta["pre_data"]["item"])
        topic_id = last_item["topic_id"]

        #  先保存原始网页内容
        loader1 = ItemLoader(response=response, item=RawHtml())
        loader1.add_value('board', 'DFCFW_guba')
        loader1.add_value('url', response.url)
        loader1.add_value('datetime', datetime.datetime.now())
        loader1.add_value('content', response.text)
        # loader1.add_value('publish_time', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
        loader1.add_value('spider_time', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

        item1 = loader1.load_item()
        yield item1

        #  保存评论内容即可
        for comment_div in response.xpath("//div[contains(@class, 'zwli clearfix')]"):
            reply_item = Replay()
            publish_user_info = comment_div.xpath("./div[@class='data']/@data-json").extract_first(default=None)
            if publish_user_info:
                publish_user_info = json.loads(publish_user_info)
                user_id = publish_user_info["user_id"]
                user_name = publish_user_info["user_nickname"]
                influence = publish_user_info["user_influ_level"]
                forum_age = publish_user_info["user_age"]
                user_name2 = publish_user_info["user_name"]  # 用于生成用户的主页id
                reply_item["publish_user_id"] = user_id
                reply_item["publish_user"] = user_name
                reply_item["forum_age"] = forum_age
                reply_item["influence"] = influence
            publish_user_info_href = comment_div.xpath(".//div[@class='zwliimg']//a/@href").extract_first()
            _publish_time = comment_div.xpath(".//div[@class='zwlitime']").re("\d{4}\-\d{2}\-\d{2} \d{2}\:\d{2}\:\d{2}")
            publish_time = deal_publish_time(_publish_time[0]) if _publish_time else None
            comment_id = comment_div.xpath("./@data-huifuid").extract_first()
            _content = comment_div.xpath('.//div[contains(@class, "stockcodec")]//div[@class="short_text"]//text()').extract()
            reply_to = comment_div.xpath(".//div[@class='zwlitalkbox clearfix']/div[@class='zwlitalkboxtext ']/@data-huifuid").extract_first(default=None)
            content = "".join(_content)
            reply_item["publish_user_href"] = publish_user_info_href
            reply_item["publish_time"] = publish_time
            reply_item["topic_id"] = str(topic_id)
            reply_item["replay_id"] = comment_id
            reply_item["replay_to"] = str(reply_to)
            reply_item["content"] = content
            yield reply_item

        next_url = deal_next_page(response)
        response_copy_headers = deepcopy(response.request.headers)
        if next_url:
            yield scrapy.Request(url=next_url, headers=response_copy_headers, meta={"pre_data": {
                "item": last_item
            }}, callback=self.parse_forum_next)


    def parse_person(self, response):
        # jsdata = response.selector.re("itemdata = (\{.*\})\;")
        # datajson = json.loads(jsdata[0])

        #  保存原始网页信息
        loader1 = ItemLoader(response=response, item=RawHtml())
        loader1.add_value('board', 'DFCFW_iguba')
        loader1.add_value('url', response.url)
        loader1.add_value('datetime', datetime.datetime.now())
        loader1.add_value('content', response.text)
        loader1.add_value('spider_time', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

        item1 = loader1.load_item()
        yield item1

        loader2 = ItemLoader(response=response, item=PublisherInfo())
        loader2.add_value("publish_user_href", response.url)
        loader2.add_xpath("publish_user_name", '//div[@class="taname"]/text()', lambda x: x[0].strip())
        loader2.add_xpath("influence", "//div[@id='influence']//span/@data-influence", lambda x: int(x[0]) if x else 0)
        loader2.add_xpath("publish_user_id",
                          "//div[@class='gbbody']//div[@class='tanums']//td/a[contains(@href, 'fans')]/em/../../a/@href",
                          lambda x: x[0].strip("/").strip("/fans") if x else "")
        loader2.add_value("his_stock_count",
                          response.xpath("//div[@class='gbbody']//div[@class='tanums']//td[1]/a/em/text()").extract_first(),
                          lambda x: int(x[0].strip()) if x else 0)
        loader2.add_xpath("fans_count",
                          "//div[@class='gbbody']//div[@class='tanums']//td/a[contains(@href, 'fans')]/em/text()",
                          lambda x: int(x[0].strip()) if x else 0)
        loader2.add_xpath("person_he_care_count",
                          "//div[@class='gbbody']//div[@class='tanums']//td/a[contains(@href, 'tafollow')]/em/text()",
                          lambda x: int(x[0].strip()) if x else 0)
        loader2.add_value("visit_count",
                          response.xpath('//div[@class="sumfw"]//span[contains(text(), "次")]/text()').extract_first(),
                          lambda x: x[0].strip("次") if x else 0)
        loader2.add_value("register_time", response.xpath("//div[@id='influence']//span[@style]").re("\((.*)\)"))
        loader2.add_value("forum_age", response.xpath("//div[@id='influence']//span/text()").extract_first(0))
        loader2.add_xpath("attention_field", '//div[@id="influence"]/a[@target]/text()')
        loader2.add_xpath("attention_field_url", '//div[@id="influence"]/a[@target]/@href')
        loader2.add_xpath("abstract", '//div[@class="taintro"]/text()')

        loader2.add_value("fans", response.url+"/fans")
        loader2.add_value("his_stock", "http://iguba.eastmoney.com/interf/stocklist.aspx")
        loader2.add_value("person_he_care", response.url + "/tafollow")

        item2 = loader2.load_item()
        yield item2


        # todo: fans,stock_focused_on 都需要在filepipeline中写ajax 请求吗，将剩下的字段补充完整。







