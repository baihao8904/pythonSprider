# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
import time
import urllib

class XiantianqiPipeline(object):
    def process_item(self, item, spider):
        today = time.strftime('%Y-%m-%d',time.localtime())
        filename = 'xiantianqi'+today+'.txt'
        with open(filename,'a') as fp:
            # fp.write(item['PM_num'] + '\t')
            fp.write(item['cityDate']+'\t')
            fp.write(item['week'] + '\t')
            imgName = os.path.basename(item['img'])
            fp.write(imgName + '\t')
            if os.path.exists(imgName):
                pass
            else:
                with open(imgName,'wb') as fp:
                    response = urllib.request.urlopen(item['img'])
                    fp.write(response.read())
            fp.write(item['temperature'] + '\t')
            fp.write(item['weather'] + '\t')
            fp.write(item['wind'] + '\n')
            time.sleep(0.5)
        return item
