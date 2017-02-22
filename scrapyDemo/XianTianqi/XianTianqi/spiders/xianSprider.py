# -*- coding: utf-8 -*-
import scrapy
from XianTianqi.items import XiantianqiItem

class XianspriderSpider(scrapy.Spider):
    name = "xianSprider"
    allowed_domains = ["xian.tianqi.com"]
    start_urls = ['http://xian.tianqi.com/']

    def parse(self, response):
        # pmselector = response.xpath('//div[@class="ikqwr ikqwr04"]/i/text()').extract()[0]
        subSelector = response.xpath('//div[@class="tqshow1"]')
        items = []
        for sub in subSelector:
            item = XiantianqiItem()
            # item['PM_num'] = pmselector
            citydate =''
            for cityDate in sub.xpath('./h3//text()').extract():
                citydate += cityDate
            item['cityDate'] = citydate
            item['week'] = sub.xpath('./p//text()').extract()[0]
            item['img'] = sub.xpath('./ul/li[1]/img/@src').extract()[0]
            # temps = ''
            temps = ''.join(sub.xpath('./ul/li[2]//text()').extract())
            item['temperature'] = temps
            item['weather']  = sub.xpath('./ul/li[3]//text()').extract()[0]
            item['wind'] = sub.xpath('./ul/li[4]//text()').extract()[0]
            items.append(item)
        return items
