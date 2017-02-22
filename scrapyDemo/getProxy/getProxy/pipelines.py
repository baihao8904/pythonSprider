# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import time


class GetproxyPipeline(object):
    def process_item(self, item, spider):
        thetime = time.strftime('%Y-%m-%d',time.localtime())
        filename = thetime+'proxy.txt'
        with open('./'+filename,'a+') as fp:
            fp.write(item['ip'].strip() + '\t')
            fp.write(item['port'].strip() + '\t')
            fp.write(item['type'].strip() + '\t')
            fp.write(item['loction'].strip() + '\t')
            fp.write(item['protocol'].strip() + '\t')
            fp.write(item['source'].strip() + '\n')
        return item

