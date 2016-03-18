# -*- coding: utf-8 -*-
from scrapy.selector import Selector
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors.sgml import SgmlLinkExtractor
from scrapy.linkextractors import LinkExtractor
from paipaidai.items import PaipaidaiItem
from scrapy import Request
class PaipaidaiSpider(CrawlSpider):
    name="paipaidai"
    allowed_domains=["www.ppdai.com"]
    start_urls=[]
    for index in range(1000000,1020000):
        start_urls.append("http://www.ppdai.com/list/"+str(index))
    def parse(self, response):
        sel=Selector(response)
        item=PaipaidaiItem()
        # 分开爬，需要哪个就把其他的注释掉
        item['username']=sel.xpath('//a[@class="username"]/text()').extract()
        item['process']=sel.xpath('//div[@class="item w260"]/text()').extract()
        item['bidinfo']=sel.xpath('//span[@class="bidinfo"]/text()').extract()
        item['money']=sel.xpath('//div[@class="newLendDetailMoneyLeft"]/dl[1]/dd/text()').extract()
        item['rate']=sel.xpath('//div[@class="newLendDetailMoneyLeft"]/dl[2]/dd/text()').extract()
        item['timelimit']=sel.xpath('//div[@class="newLendDetailMoneyLeft"]/dl[3]/dd/text()').extract()
        item['finishtime']=sel.xpath('//span[@class="countdown_row countdown_amount"]/text()').extract()
        yield item
    
