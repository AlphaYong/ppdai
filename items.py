# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field

class PaipaidaiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
class PaipaidaiItem(Item):
    # 分开爬的，需要哪个就把其他的注释掉
    # 两个程序分别爬取
    username=Field()
    process=Field()
    bidinfo=Field()
    money=Field()
    rate=Field()
    timelimit=Field()    
    finishtime=Field()
    # 另外的一组
    shenfen=Field()
    borrow_honor=Field()
    lend_honor=Field()
    sex=Field()
    old=Field()
    user_name=Field()
