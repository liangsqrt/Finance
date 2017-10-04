# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from Finance.items import forumdata
import pymongo



class FinancePipeline(object):
    def process_item(self, item, spider):
        return item


class DFCFWPipeline(object):
    def __init__(self):
        self.client=pymongo.MongoClient('localhost',27017)
        self.COL=self.client['Finance']
        self.DB=self.COL['DFCFW10_4']

    def process_item(self,item,spider):
        if isinstance(item,forumdata):
            try:
                self.DB.insert(dict(item))
                print '成功插入到数据一个'
            except Exception as e:
                print e
    def add_index(self):
        self.DB.ensure_index('url',unique=True)


if __name__ == '__main__':
    thisclass=DFCFWPipeline()
    thisclass.add_index()