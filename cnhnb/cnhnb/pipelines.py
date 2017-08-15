# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


from scrapy.exceptions import DropItem
import pymongo


class MongoPipeline(object):
    def open_spider(self, spider):
        self.client = pymongo.MongoClient("mongodb://10.10.51.30:27017")
        self.db=self.client["test4"]
    def close_spider(self, spider):
        self.client.close()
    def process_item(self, item, spider):
        if item.get('title'):
            self.db['ProductionInfo'].update_one({"_id": "test"}, {"$inc": {"count": 1}})
            self.db['news'].insert_one(item)
        else:
            self.db['category'].insert_one(item)
        return item