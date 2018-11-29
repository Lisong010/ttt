# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WurenjiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title=scrapy.Field()
    date=scrapy.Field()
    zuozhe=scrapy.Field()
    laiyuan=scrapy.Field()
    article=scrapy.Field()
    image=scrapy.Field()
