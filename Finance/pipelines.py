# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from Finance.items import forumdata
from Finance.items import forumhtmlpage
from Finance.items import DFCFWpublisher
from Finance.other_moudle import create_filename
import pymongo
import json
import platform
import hashlib
import time
from Finance.other_moudle.pipeline_nameEN_to_nameCN import getNameCN
import os






BASIC_FILE="E:/data_DFCFW_news"
BASIC_FILE2='E:/data2_DFCFW_news_'
if platform.system()=='Linux':#BigDATA's workstation
    BASIC_FILE='/home/spider/data_DFCFW_news'
    BASIC_FILE2='/home/spider/data2_DFCFW_news_'





class FinancePipeline(object):
    def process_item(self, item, spider):
        return item


class DFCFWPipeline(object):
    def __init__(self):
        self.client=pymongo.MongoClient('localhost',27017)
        self.COL=self.client['Finance']
        self.DB=self.COL['DFCFW10_4']
        self.DB_DFCFW_relation=self.COL['DFCFW_md5_url']
        self.DB_publish_user=self.COL['DFCFW_publish_user']

    def process_item(self,item,spider):
        if isinstance(item,forumhtmlpage):
            item_dict = dict(item)
            plant_form = item['board']
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


    def add_index(self):
        self.DB.ensure_index('url',unique=True)
    def close_spider(self,spider):
        self.client.close()


class save_data_to_file(object):
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
        plant_form=spider.name
        publish_time=item['publish_time']
        urlOruid=item['url']
        newsidOrtid=item['id']
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


if __name__ == '__main__':
    thisclass=DFCFWPipeline()
    thisclass.add_index()