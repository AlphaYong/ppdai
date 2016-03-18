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
    rules=[
            Rule(LinkExtractor(allow=(r'http://www.ppdai.com/user/'),restrict_xpaths=('//a[@class="username"]')),callback="parse_item",follow=True)      
    ]


    def parse_item(self,response):
        sel=Selector(response)
        item=PaipaidaiItem()
        # 需要哪个就把其他的注释掉
        item['borrow_honor']=sel.xpath('//li[@class="honor_li"]/p[1]/span[1]/span[1]/text()').extract()
        item['lend_honor']=sel.xpath('//li[@class="honor_li"]/p[2]/span[1]/span[1]/text()').extract()
        item['sex']=sel.xpath('//li[@class="user_li"]/p[1]/span[1]/text()').extract()
        item['old']=sel.xpath('//li[@class="user_li"]/p[1]/span[2]/text()').extract()
        item['user_name']=sel.xpath('//p[@class="user-name"]/a[1]/text()').extract()
        item['shenfen']=sel.xpath('//li[@class="user_li"]/p[2]/text()').extract()
        return item
