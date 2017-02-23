# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import time
import os

class MeijuPipeline(object):
    def process_item(self, item, spider):
        thetime = time.strftime('%Y-%m-%d', time.localtime())
        filename = thetime + '.json'
        thepath = os.path.dirname(__file__)
        with open(filename, 'a+') as fp:
            fp.write(json.dumps(dict(item),ensure_ascii=False)+'\n')
        return item