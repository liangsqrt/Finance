# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from Finance.items import forumdata
from Finance.items import forumhtmlpage
from settings import Finance_DFCFW_tieba_path
from Finance.other_moudle import create_filename
import pymongo
import json



class FinancePipeline(object):
    def process_item(self, item, spider):
        return item


class DFCFWPipeline(object):
    def __init__(self):
        self.client=pymongo.MongoClient('localhost',27017)
        self.COL=self.client['Finance']
        self.DB=self.COL['DFCFW10_4']
        self.DB_DFCFW_relation=self.COL['DFCFW_md5_url']

    def process_item(self,item,spider):
        if isinstance(item,forumdata):
            try:
                self.DB.insert(dict(item))
                print '成功插入到数据一个'
            except Exception as e:
                print e

        if isinstance(item,forumhtmlpage):
            forumhtmlpage_dict=dict(item)
            date,urlmd5=create_filename.DFCFW_forumdata_name(url=forumhtmlpage_dict['mainurl'],datetime=forumhtmlpage_dict['publish_time'])
            file_finally=Finance_DFCFW_tieba_path+'/'+date+'/'+urlmd5
            create_filename.checkfile(file_finally)
            with open(file_finally,'w+') as fl:
                json.dump(forumhtmlpage_dict,fl)
                self.DB_DFCFW_relation.insert(
                    {
                        urlmd5:forumhtmlpage_dict['mainurl']#mongodb里边key的值不可以是.的内容
                    }
                )

    def add_index(self):
        self.DB.ensure_index('url',unique=True)
    def close_spider(self,spider):
        self.client.close()


if __name__ == '__main__':
    thisclass=DFCFWPipeline()
    thisclass.add_index()