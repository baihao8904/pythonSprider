# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import time
import urllib.request
import os

class QiubaiPipeline(object):
    def process_item(self, item, spider):
        today = time.strftime('%Y-%m-%d',time.localtime())
        filename = today+'.txt'
        imgDir = 'img'
        if not os.path.exists(imgDir):
            os.mkdir(imgDir)
        with open(filename,'a+') as fp:
            fp.write('*'*50 + '\n')
            fp.write('author:\t %s\n'%item['author'])
            fp.write(('content:%s\n'%item['content']))
            try:
                imgUrl = item['img'][0]
            except IndexError:
                pass
            else:
                imgName = os.path.basename(imgUrl)
                fp.write('img:\t%s\n'%imgName)
                imgPath = imgDir+'/'+imgName
                with open(imgPath,'wb') as fpi:
                    response = urllib.request.urlopen(imgUrl)
                    fpi.write(response.read())
            fp.write('fun:\t%s\ttalkNums:\t%s\n'%(item['funNum'],item['talkNum']))
            fp.write('*' * 50 + '\n')
        with open('./content.txt','a+') as fpc:
            fpc.write(item['content'])
        return item