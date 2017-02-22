# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class XiantianqiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # PM_num = scrapy.Field()
    cityDate = scrapy.Field()
    week = scrapy.Field()
    temperature = scrapy.Field()
    weather =scrapy.Field()
    img = scrapy.Field()
    wind = scrapy.Field()