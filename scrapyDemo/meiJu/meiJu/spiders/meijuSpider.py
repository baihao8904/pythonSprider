# -*- coding: utf-8 -*-
import scrapy
from meiJu.items import MeijuItem

class MeijuspiderSpider(scrapy.Spider):
    name = "meijuSpider"
    allowed_domains = ["meijutt.com"]
    start_urls = ['http://www.meijutt.com/new100.html']

    def parse(self, response):
        subSelector = response.xpath('//ul[@class="top-list  fn-clear"]/li')
        items = []
        for sub in subSelector:
            item = MeijuItem()
            item['Name'] = sub.xpath('.//h5/a/text()').extract()[0]
            try:
                item['state'] = sub.xpath('.//span/font/text()').extract()[0]
            except:
                item['state'] = '已完结'
            item['tvstation'] = sub.xpath('.//span[@class="mjtv"]/text()').extract()
            item['updateTime'] = sub.xpath('.//div[@class="lasted-time new100time fn-right"]/text() | .//div/font/text()').extract()[0]
            items.append(item)
        return items
