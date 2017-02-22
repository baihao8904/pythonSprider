# -*- coding: utf-8 -*-
import scrapy
from todayMovie.items import TodaymovieItem

class XianmoviespriderSpider(scrapy.Spider):
    name = "XianMovieSprider"
    allowed_domains = ["mtime.com"]
    start_urls = ['http://theater.mtime.com/China_Shanxi_Province_Xian/']

    def parse(self, response):
        subSelector = response.xpath('//div[@class="othermovie fr"]/ul/li')
        items=[]
        for sub in subSelector:
            item = TodaymovieItem()
            item['movieName'] = sub.xpath('./dl/dt/a/text()').extract()
            items.append(item)
        return items
