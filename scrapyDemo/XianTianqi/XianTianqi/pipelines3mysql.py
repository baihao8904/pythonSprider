import pymysql
import os

class XiantianqiPipeline(object):
    def process_item(self,item,spider):
        cityDate = item['cityDate'].encode('utf-8')
        week = item['week'].encode('utf-8')
        weather = item['weather'].encode('utf-8')
        temperature = item['temperature'].encode('utf-8')
        wind = item['wind'].encode('utf-8')
        img = os.path.basename(item['img'])

        connection = pymysql.connect(
            host = 'localhost',
            port = 3306,
            user = 'root',
            passwd = 'baihao1234',
            db = 'scrapy',
            charset = 'utf8'
        )
        cur = connection.cursor()
        theset = (cityDate,week,img,temperature,weather,wind)
        sql ="INSERT INTO xianWeather(cityDate,week,img,tempurture,weather,wind) values(%s,%s,%s,%s,%s,%s)"
        cur.execute(sql,theset)
        cur.close()
        connection.commit()
        connection.close()

        return item