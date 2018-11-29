# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo

class WurenjiPipeline(object):
    def __init__(self):
        myclient=pymongo.MongoClient('mongodb://127.0.0.1:27017')
        mydb=myclient['wurenji']
        self.mycol=mydb['xinxi']
    def process_item(self, item, spider):
        item=dict(item)
        self.mycol.insert(item)
        return item
