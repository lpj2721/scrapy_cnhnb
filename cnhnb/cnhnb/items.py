# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CnhnbItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class CategoryItem(scrapy.Item):
    name = scrapy.Field()
    _id = scrapy.Field()
    parent_id = scrapy.Field()
    link = scrapy.Field()
    pass


class NewsItem(scrapy.Item):
    title = scrapy.Field()
    tag = scrapy.Field()
    pic_d = scrapy.Field()
    abstract = scrapy.Field()
    create_time = scrapy.Field()
    main_body = scrapy.Field()


