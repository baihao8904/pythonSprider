# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MeijuItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Name = scrapy.Field()
    state = scrapy.Field()
    tvstation = scrapy.Field()
    updateTime = scrapy.Field()
