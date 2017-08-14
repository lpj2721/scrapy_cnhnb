#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Tommy on 2017/8/149:56
import scrapy
from scrapy.http.response import Response
from cnhnb.items import CategoryItem
from cnhnb.fun_lib import date_time, get_id
import sys
reload(sys)                      # reload 才能调用 setdefaultencoding 方法
sys.setdefaultencoding('utf-8')
str_type = sys.getfilesystemencoding()


class CnhnbSpider(scrapy.spiders.Spider):
    name = "cnhnb"
    allowed_domains = ["cnhnb.com"]
    start_urls = [
        "http://www.cnhnb.com/xt/wzcz/"
    ]

    def parse(self, response):
        cate_item = CategoryItem()
        node_item = CategoryItem()
        print 2222
        for cate in response.xpath('/html/body/div[3]/div[1]/div/dl'):
            cate_item['name'] = cate.xpath('./dt/text()')[0].extract().decode('utf-8')
            cate_item['_id'] = get_id()
            cate_item['parent_id'] = 1
            cate_item['link'] = " "
            for node in cate.xpath('./dd'):
                node_item['name'] = node.xpath('./a/text()')[0].extract().decode('utf-8')
                node_item['_id'] = get_id()
                node_item['parent_id'] = cate_item['_id']
                node_item['link'] = node.xpath('./a/@href')[0].extract()
                yield node_item
            yield cate_item

