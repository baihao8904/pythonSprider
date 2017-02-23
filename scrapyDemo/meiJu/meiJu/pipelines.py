# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
import time


class MeijuPipeline(object):
    def process_item(self, item, spider):
        thetime = time.strftime('%Y-%m-%d',time.localtime())
        filename = thetime+'.txt'
        thepath = os.path.dirname(__file__)
        with open(filename,'a+') as fp:
            fp.write(item['Name']+'\t')
            fp.write(item['state'] + '\t')
            if len(item['tvstation']) ==0:
                fp.write('unknown'+'\t')
            else:
                fp.write(item['tvstation'][0] + '\t')
            fp.write(item['updateTime'] + '\n')
        return item
