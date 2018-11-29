# -*- codeing:utf-8 -*-
from scrapy.spiders import CrawlSpider,Rule
from scrapy.selector import Selector
from scrapy.linkextractors import LinkExtractor

class RenGongZhiNeng(CrawlSpider):
    name='rgzn'
    allower_domains = []
    start_urls = ['http://www.ailab.cn/?page=1']

    rules=(
        Rule(LinkExtractor(allow='http://www.ailab.cn/?page=\d+'),follow=True),
        Rule(LinkExtractor(allow='http://(.*?).html',restrict_css='ul.list_jc a'),
             callback='parse_item',follow=False,)
    )
    def parse_item(self,response):
        print(response.url)