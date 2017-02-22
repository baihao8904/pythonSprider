# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import time


class TodaymoviePipeline(object):
    def process_item(self, item, spider):
        now = time.strftime('%Y-%m-%d',time.localtime())
        fileName = 'Xian'+now+'.txt'
        path = 'E:\pythonexercise\pythonSprider\scrapyDemo\\todayMovie\\'
        with open(fileName,'a+') as fp:
            fp.write(item['movieName'][0]+'\n')
        return item
