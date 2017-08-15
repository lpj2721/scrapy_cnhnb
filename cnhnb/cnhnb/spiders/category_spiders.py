#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Tommy on 2017/8/149:56
import scrapy
import requests
import base64
from lxml import etree
from cnhnb.items import CategoryItem, NewsItem
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
        news_item = NewsItem()
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
                news_resp = etree.HTML(requests.get(node_item['link']).text)
                print 3333
                for each in news_resp.xpath('//*[@id="list"]/div'):
                    news_item['_id'] = get_id()
                    news_item['link'] = each.xpath('a/@href')[0]
                    news_item['desc_pic'] = each.xpath('a/img/@src')[0]
                    news_item['title'] = each.xpath('div/a/p[1]/text()')[0]
                    if each.xpath('div/a/p[3]/text()'):
                        news_item['abstract'] = each.xpath('div/a/p[3]/text()')[0]
                    else:
                        news_item['abstract'] = ""
                    news_item['tag'] = each.xpath('div/a/p[1]/span/text()')[0]
                    news_item['create_time'] = date_time()
                    news_item['source'] = "惠农网"
                    news_item['pic_urls'] = []
                    news_item['subtitle'] = ""
                    news_item['type'] = node_item['_id']
                    news_content = etree.HTML(requests.get(news_item['link']).text)
                    if news_content.xpath('//div[@class="view-des"]'):
                        content = etree.tostring(news_content.xpath('//div[@class="view-des"]')[0])
                        news_item['contents'] = base64.encodestring(content)
                        yield news_item
                    else:
                        news_item['contents'] = " "
                    pass
                yield node_item
            yield cate_item

