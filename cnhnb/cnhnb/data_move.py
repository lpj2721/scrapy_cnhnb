#!/usr/bin/env python
# encoding: utf-8
"""
@author: WL
@time: 2017/8/14 17:33
"""
import requests
import pymongo
client = pymongo.MongoClient("mongodb://10.10.51.30:27017")
test_db = client['test4']
n_client = pymongo.MongoClient("mongodb://10.10.51.100:7003")
n_db = n_client['protoolDB']
n_db.authenticate("protoolDB", "youlu_dc_666666")
cate_url = "http://10.10.51.1:5002/api/protool/v1/category/add"
news_url = "http://10.10.51.1:5002/api/protool/v1/news/ad"


def post(url, json):
    resp = requests.post(url=url, json=json)
    return resp.json()

parent_nodes = test_db['category'].find({"parent_id": 1})
parent_total = parent_nodes.count()
# print "目录节点插入进度:{}/{}".format(t_i,total)
f_i = 0
for f_cate in parent_nodes:
    f_i += 1
    f_docs = {
        "category_name": f_cate.get('name'),
        "ancestor_id":"news",
        "icon_url": "",
        "barn":""
        }
    f_result = post(url=cate_url,json=f_docs)
    f_id = f_result['data']['category_id']
    print "目录节点插入进度:{}/{}".format(f_i, parent_total)
    cate_node = test_db['category'].find({'parent_id': f_cate.get('_id')})
    s_total = cate_node.count()
    s_i = 0
    for s_cate in cate_node:
        s_i += 1
        s_docs = {
            "category_name": s_cate.get('name'),
            "ancestor_id": f_id,
            "icon_url": "",
            "barn": ""
        }
        s_result = post(url=cate_url, json=s_docs)
        s_id = s_result['data']['category_id']
        print "二级目录节点插入进度:{}/{}".format(s_i, s_total)
        news_list = test_db['news'].find({'type': s_cate['_id']})
        news_total = news_list.count()
        news_i = 0
        for news in news_list:
            news_i += 1
            news_docs = {
                "title": news['title'],
                "subtitle": "",
                "abstract": news['abstract'],
                "contents": news['contents'],
                "type": s_id,
                "source": news['source'],
                "source_icon": "",
                "desc_pic": news['desc_pic'],
                "pic_urls": []
            }
            news_result = post(url=news_url, json=news_docs)
            print "新闻插入进度:{}/{}".format(news_i, news_total)



