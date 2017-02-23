# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class MeijuPipeline(object):
    def process_item(self, item, spider):
        connection = pymysql.connect(
            host = 'localhost',
            port = 3306,
            user = 'root',
            passwd = 'baihao1234',
            db = 'scrapy',
            charset = 'utf8'
        )

        name = item['Name']
        state = item['state']
        tvstation = item['tvstation']
        updatetime = item['updateTime']

        cursor = connection.cursor()
        theset = (name,state,tvstation,updatetime)
        sql = "INSERT INTO meiju VALUES (%s,%s,%s,%s)"
        cursor.execute(sql,theset)
        cursor.close()
        connection.commit()
        connection.close()
        return item
