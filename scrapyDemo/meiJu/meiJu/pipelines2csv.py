# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import csv
import os
import time


class MeijuPipeline(object):
    def process_item(self, item, spider):
        thetime = time.strftime('%Y-%m-%d', time.localtime())
        filename = thetime + '.csv'
        #thepath = os.path.dirname(__file__)
        aCsvWriter = csv.writer(open(filename,'a+'),lineterminator ='\n')
        fileheader = ['name','state','tvstation','updatetime']
        if open(filename).read()[0:4] =='name':
            pass
        else:
            aCsvWriter.writerow(fileheader)
        aCsvWriter.writerow([item[k] for k in item.keys()])
        return item
