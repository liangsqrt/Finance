# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from Finance.items import RawHtml
from Finance.other_moudle import create_filename
import pymongo
import json
import platform
import hashlib
import time
from Finance.other_moudle.pipeline_nameEN_to_nameCN import getNameCN
import os
import pickle
from Finance.items import *
from scrapy.pipelines.media import MediaPipeline
import scrapy
from scrapy.utils.misc import arg_to_iter
from twisted.internet.defer import DeferredList

BASIC_FILE = "E:/data_DFCFW_news"
BASIC_FILE2 = 'E:/data2_DFCFW_news_2'
if platform.system() == 'Linux':  # BigDATA's workstation
    BASIC_FILE = '/media/liang/store1/data_DFCFW_news'
    BASIC_FILE2 = '/media/liang/store1/data_DFCFW_news2'





class FinancePipeline(object):
    def process_item(self, item, spider):
        return item


class DFCFWPipeline(object):
    def __init__(self):
        self.client = pymongo.MongoClient('localhost', 27017)
        self.COL = self.client['Finance']
        self.DB = self.COL['DFCFW10_4']
        self.DB_DFCFW_relation = self.COL['DFCFW_md5_url']
        self.DB_publish_user = self.COL['DFCFW_publish_user']

    def process_item(self, item, spider):
        if isinstance(item, RawHtml):
            item_dict = dict(item)
            plant_form = item['board'][0]
            publish_time = item['publish_time'][0]
            urlOruid = item['mainurl'][0]
            newsidOrtid = item['id'][0]
            datatype = 'news'

            filename, file_path = self.create_file_str(publish_time=publish_time, plant_form=plant_form,
                                                       urlOruid=urlOruid, newsidOrtid=newsidOrtid, datatype=datatype)

            self.save_data(file_path=file_path, file=filename, full_data=item_dict)
    def create_file_str(self,publish_time,plant_form,urlOruid,newsidOrtid,datatype):
        '''
        数据文件名的生成函数，根据参数来生成1101中要求的数据文件的格式名。
        还要根据BASIC_FILE中的字段来生成相应的路径，如果没有，就自动创建。


        :param publish_time:
        :param plant_form:
        :param urlOruid:
        :param newsidOrtid:
        :param datatype:
        :return: file_path是文件的具体存储路径，注意：filename不只是文件名，还包括了前边的文件路径，比如：
                /home/spider/silence/spider_test/spider_content/具体一个1101中的文件的名称。
        '''
        try:
            publish_time_array = self.examing_datetime_format(publish_time)
            publish_time_stramp = time.mktime(publish_time_array)
            publish_time_stramp_str_13 = str(int(publish_time_stramp*1000))
        except:
            print('wrong in create publish_time_stramp_str_13')
            publish_time_stramp_str_13 = 'time_wrong'

        urlhashlib = hashlib.md5(urlOruid.encode('utf-8')).hexdigest()
        urlhashlib_str = str(urlhashlib)

        CNname = getNameCN(plant_form)

        try:
            publish_time_split_2=publish_time.split(' ')
            publish_time_split_2=[str(x) for x in publish_time_split_2]
        except Exception as e:
            publish_time_split_2=['time_wrong','time_wrong']
        filename=publish_time_stramp_str_13+'_'+CNname.replace('/','_')+'_speeches_'+str(publish_time_split_2[0])+'_'+plant_form.replace('/','_')+'_'+publish_time_stramp_str_13+'_'+urlhashlib_str

        file_path=BASIC_FILE+'/speeches'+'/'+CNname+'/'+publish_time_split_2[0]
        filename=file_path+'/'+filename#看到没有，这里就把前边的路径名加在filename之前了，所以filename不单单是一个文件名。

        return filename,file_path

    def examing_datetime_format(self,timestr):
        '''
        检测时间格式是否符合规定的一个函数。因为在实际情况中，有些网页解析出来的时间格式不对，情况比较多，因为要在文件名中用到这个字段所以这个字段比较重要，
        所以这里单独设置一个模块用来处理这些意外情况。有些网站没有publish_time，跟大数据商量好了，一律使用2018-02-01 00:00:00

        :param timestr: publsh_time
        :return: 处理过后的publish_time
        '''
        try:
            timestrlist = time.strptime(timestr, '%Y-%m-%d %H:%M:%S')
            return timestrlist
        except:
            try:
                timestrlist = time.strptime(timestr, '%Y-%m-%d %H:%M')
                return timestrlist
            except:
                try:
                    timestrlist = time.strptime(timestr, "%Y-%m-%d")
                    return timestrlist
                except:
                    print ('时间格式有误')
                    print (timestr)
                    return time.strptime('2018-02-01 00:00:00','%Y-%m-%d %H:%M:%S')

    def save_data(self,file_path, file, full_data):  # 因为后来要用到存储的时候的文件名，先要调用里边的文件名，所以生成文件名和爬取数据结果应该分开写。
        #file相当于是file_path+'/'+filename
        '''

        :param file_path: 数据存储的文件路径，
        :param file: 数据文件路径名+数据文件名
        :param full_data: 一个完成的处理过后的，只差存储了，的一个数据。
        :return: 这里已经是爬虫的末端了，
        '''
        if os.path.exists(file_path):
            with open(file, 'wb+') as cmfl:
                # json.dump(full_data, cmfl)
                # cmfl.write(full_data['content'][0])
                pickle.dump(full_data,cmfl)
        else:
            os.makedirs(file_path)
            with open(file, 'wb+') as cmfl:
                # json.dump(full_data, cmfl)
                # cmfl.write(full_data['content'][0])
                pickle.dump(full_data,cmfl)

    def add_index(self):
        self.DB.ensure_index('url',unique=True)

    def close_spider(self,spider):
        self.client.close()


class SacaDataByFile(object):
    '''
    文件存储模块，将解析出来的数据以json的格式存储到硬盘中去，路径最上边的BASIC_FILE，不是BASIC_FILE2，BASIC_FILE2在save_data_to_RemoteFile_XMX中。
    '''
    def process_item(self,item,spider):
        '''
        标准的middleware函数，具体参考官方文档。

        :param item: 从spider中解析出来的对象，或者从其它middleware中解析出来的item，具体顺序可以在setting中设置，详细参见官方帮助文档。
        :param spider: spider的名称，可以提取spider中的某些字段，比如spdier_name
        :return: 这里没有返回对象，直接存储到了本地文件中。   如有需要，具体如何返回数据，参见官方文档。
        '''
        item_dict=dict(item)
        plant_form=spider.name[0]
        publish_time=item['publish_time'][0]
        urlOruid=item['url'][0]
        newsidOrtid=item['id'][0]
        datatype='news'

        filename,file_path=self.create_file_str(publish_time=publish_time,plant_form=plant_form,urlOruid=urlOruid,newsidOrtid=newsidOrtid,datatype=datatype)

        self.save_data(file_path=file_path,file=filename,full_data=item_dict)

        # try:
        #     self.save_data(file_path='E:/data_all_xizang',file='E:/data_all_xizang/'+filename.split('/')[-1],full_data=item_dict)
        # except Exception as e:
        #     print e

        return item

    def create_file_str(self,publish_time,plant_form,urlOruid,newsidOrtid,datatype):
        '''
        数据文件名的生成函数，根据参数来生成1101中要求的数据文件的格式名。
        还要根据BASIC_FILE中的字段来生成相应的路径，如果没有，就自动创建。


        :param publish_time:
        :param plant_form:
        :param urlOruid:
        :param newsidOrtid:
        :param datatype:
        :return: file_path是文件的具体存储路径，注意：filename不只是文件名，还包括了前边的文件路径，比如：
                /home/spider/silence/spider_test/spider_content/具体一个1101中的文件的名称。
        '''
        try:
            publish_time_array = self.examing_datetime_format(publish_time)
            publish_time_stramp=time.mktime(publish_time_array)
            publish_time_stramp_str_13=str(int(publish_time_stramp*1000))
        except:
            print ('wrong in create publish_time_stramp_str_13')
            publish_time_stramp_str_13='time_wrong'

        urlhashlib=hashlib.md5(urlOruid.encode('utf-8')).hexdigest()
        urlhashlib_str=str(urlhashlib)

        CNname=getNameCN(plant_form)

        try:
            publish_time_split_2=publish_time.split(' ')
            publish_time_split_2=[str(x) for x in publish_time_split_2]
        except Exception as e:
            publish_time_split_2=['time_wrong','time_wrong']
        filename=publish_time_stramp_str_13+'_'+CNname+'_speeches_'+str(publish_time_split_2[0])+'_'+plant_form+'_'+publish_time_stramp_str_13+'_'+urlhashlib_str

        file_path=BASIC_FILE+'/speeches'+'/'+CNname+'/'+publish_time_split_2[0]
        filename=file_path+'/'+filename#看到没有，这里就把前边的路径名加在filename之前了，所以filename不单单是一个文件名。

        return filename,file_path

    def examing_datetime_format(self,timestr):
        '''
        检测时间格式是否符合规定的一个函数。因为在实际情况中，有些网页解析出来的时间格式不对，情况比较多，因为要在文件名中用到这个字段所以这个字段比较重要，
        所以这里单独设置一个模块用来处理这些意外情况。有些网站没有publish_time，跟大数据商量好了，一律使用2018-02-01 00:00:00

        :param timestr: publsh_time
        :return: 处理过后的publish_time
        '''
        try:
            timestrlist = time.strptime(timestr, '%Y-%m-%d %H:%M:%S')
            return timestrlist
        except:
            try:
                timestrlist = time.strptime(timestr, '%Y-%m-%d %H:%M')
                return timestrlist
            except:
                try:
                    timestrlist = time.strptime(timestr, "%Y-%m-%d")
                    return timestrlist
                except:
                    print ('时间格式有误')
                    print (timestr)
                    return time.strptime('2018-02-01 00:00:00','%Y-%m-%d %H:%M:%S')

    def save_data(self,file_path, file, full_data):  # 因为后来要用到存储的时候的文件名，先要调用里边的文件名，所以生成文件名和爬取数据结果应该分开写。
        #file相当于是file_path+'/'+filename
        '''

        :param file_path: 数据存储的文件路径，
        :param file: 数据文件路径名+数据文件名
        :param full_data: 一个完成的处理过后的，只差存储了，的一个数据。
        :return: 这里已经是爬虫的末端了，
        '''
        if os.path.exists(file_path):
            with open(file, 'w+') as cmfl:
                json.dump(full_data, cmfl)
        else:
            os.makedirs(file_path)
            with open(file, 'w+') as cmfl:
                json.dump(full_data, cmfl)


class SaveDataByMongo(object):
    def process_item(self, item, spider):
        try:
            mongoitem = item.__create_sqlalchemy_item__()
            mongoitem.save()
        except Exception as e:
            print(e)
        # return item


class DFCFWFansPipeline(MediaPipeline):
    def open_spider(self, spider):
        self.headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
        }
        self.spiderinfo = self.SpiderInfo(spider)

    def get_media_requests(self, item, info):
        stock_url = item["fans"]
        yield scrapy.Request(url=stock_url, headers=self.headers, method="GET")

    def item_completed(self, results, item, info):
        del item["fans"]
        del item["person_he_care"]
        if results[0][0]:
            try:
                response = results[0][1]
                fanslist = response.xpath("//div[@class='tasidb2']//ul[@class='tasiderplist']//li/a/@href").extract()
                fanslist = [x.strip().strip("/") for x in fanslist]
                person_he_care = response.xpath("//div[@class='tasidb1']//ul[@class='tasiderplist']//li/a/@href").extract()
                person_he_care = [x.strip().strip("/") for x in person_he_care]
                item["person_he_care"] = list(set(person_he_care))
                item["fans"] = list(set(fanslist))
            except Exception as e:
                print(e)
        return item

    def process_item(self, item, spider):
        if isinstance(item, PublisherInfo):
            info = self.spiderinfo
            requests = arg_to_iter(self.get_media_requests(item, info))
            dlist = [self._process_request(r, info) for r in requests]
            dfd = DeferredList(dlist, consumeErrors=1)
            return dfd.addCallback(self.item_completed, item, info)
        else:
            return item


class DFCFWStockPipeline(MediaPipeline):
    def open_spider(self, spider):
        self.headers = {
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
                "Cookie": "st_si=72747346219909; qgqp_b_id=96405d9f780665ad03d6328aed2f2b57; p_origin=https%3A%2F%2Fpassport2.eastmoney.com; ct=r-R8ChPJZmqF1WY8IFIigHY1y0Ii6aG7t81fUpRbYPTI7p4ST3qEeEZ-5zm7RkU8tctDvFuEguPZAuCwsxL-krS3IrmuOXf-Nf0ErcV9dPJv-iMKqrjXSH1aVQyULlHS12K008QorQQJjzf_8F-e7lYE8vhB2RZxeejVQMSYst4; ut=FobyicMgeV60R-wNFHdtrN17mhW5wDy4v9r6x1eY-wyk7BD3Q4qOgM5u27e--2Vz5DlQpGggkVwBNjS7W_QRxA8pE2WRgcRlN8g8sWEUcydlBcAo-fAhe6GdYEiUKU5cXaxmXK2-PdtHHbpdN-C_8naI7oopKJ4voq_MnOn5BPphm0WcCMVCF-4fhE-_81Q8Mh3kZQMaelEYkTD4K_gMOSoLu3VHmAkOFttp7mo6B7n9rcivNTTCVmOPZlumS1nO06LZC4rOFN3ARQ0pk-8czrDSXaInGiWE; pi=3564345589542852%3bm3564345589542852%3breboot1%3bUfUUbcfW0RZ6JgBqknIa7iXB6V0cK%2f7MSaPoGYn%2fcbebGw3tNd47%2fCmy6Hwq8U0KzZp50dXVCdGF82VMh8b7%2ffMqfvhlF3Hx8EZt18CiRG2A%2fvELeik%2bQm0iSvIueM2EGrpUoQKEq1paU%2bSwiXvijY5Ypucm0N02TahJFsmXSkmYV0nGFhhv4LxPvb2n5v3jwX6AR0v4%3b5BztCv8%2b5Rte5R%2fTSvHFFFYy2ifsGzgiw127Fx2bEKYxS5vnCEDeZJi4Cf6RUl%2fCEIytmrzw1DUuBNwPQUymUeDbS7I3oWW02QAfsKicZc%2bdHnL%2bMRehssQK2z67KBymOm%2fXXlLdAeygTa1Do%2f1YnEtPgssyZA%3d%3d; uidal=3564345589542852reboot1; sid=137744318; vtpst=|; st_asi=delete; st_pvi=06651445649880; st_sp=2019-06-06%2005%3A01%3A55; st_inirUrl=https%3A%2F%2Fwww.baidu.com%2Flink; st_sn=14; st_psi=20190606055018370-117005300001-8560595066",
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
            }
        self.data = {
            "action": "gettastock",
            "type": "hs",
            "uid": "4162005331760506"
        }
        self.spiderinfo = self.SpiderInfo(spider)

    def get_media_requests(self, item, info):
        stock_url = item["his_stock"]
        if isinstance(item["his_stock_count"], list):  # 莫名其妙
            item["his_stock_count"] = item["his_stock_count"][0]
        self.data["uid"] = item["publish_user_id"]
        yield scrapy.FormRequest(url=stock_url, headers=self.headers, method="post", formdata=self.data)

    def item_completed(self, results, item, info):
        del item["his_stock"]
        if results[0][0]:
            response = results[0][1]
            try:
                stock_list = json.loads(response.text)
                stock_list = [x.strip().split("|")[0] for x in stock_list["data"]["stklist"].split(",")]
                item["his_stock"] = stock_list
            except Exception as e:
                print(e)
        return item

    def process_item(self, item, spider):
        if isinstance(item, PublisherInfo):
            info = self.spiderinfo
            requests = arg_to_iter(self.get_media_requests(item, info))
            dlist = [self._process_request(r, info) for r in requests]
            dfd = DeferredList(dlist, consumeErrors=1)
            return dfd.addCallback(self.item_completed, item, info)
        else:
            return item


class DFCFWPersonHeCarePipeline(MediaPipeline):
    """
    没必要，在跟fans页面的内容一模一样
    """
    def open_spider(self, spider):
        self.headers = {
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
            }
        self.spiderinfo = self.SpiderInfo(spider)

    def get_media_requests(self, item, info):
        person_her_care = item["person_he_care"]
        yield scrapy.FormRequest(url=person_her_care, headers=self.headers, method="GET")

    def item_completed(self, results, item, info):
        del item["person_he_care"]
        if results[0][0]:
            response = results[0][1]
            try:
                stock_list = json.loads(response.text)
                stock_list = [x.strip().split("|")[0] for x in stock_list["data"]["stklist"].split(",")]
                item["his_stock"] = stock_list
            except Exception as e:
                print(e)

        print(item)

    def process_item(self, item, spider):
        if isinstance(item, PublisherInfo):
            info = self.spiderinfo
            requests = arg_to_iter(self.get_media_requests(item, info))
            dlist = [self._process_request(r, info) for r in requests]
            dfd = DeferredList(dlist, consumeErrors=1)
            return dfd.addCallback(self.item_completed, item, info)
        else:
            return item



if __name__ == '__main__':
    thisclass=DFCFWPipeline()
    thisclass.add_index()