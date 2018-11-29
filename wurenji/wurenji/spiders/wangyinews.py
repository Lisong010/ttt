# -*- codeing:utf-8 -*-

from scrapy.spiders import CrawlSpider,Rule
from scrapy.selector import Selector
from scrapy.linkextractors import LinkExtractor
import scrapy

class WangyiSpider(CrawlSpider):
    name='wangyi_news'
    allower_domains=[]
    start_urls=['http://tech.163.com/special/gd2016/']

    # def start_requests(self):
    #     for i in range(2,16):
    #         url = 'http://tech.163.com/special/gd2016/'
    #         urls='http://tech.163.com/special/gd2016_0'+str(i)+'/'
    #         if i<=9:
    #             urls = 'http://tech.163.com/special/gd2016_0' + str(i) + '/'
    #         else:
    #             urls='http://tech.163.com/special/gd2016_'+str(i)+'/'
    #         #写俩yield就好了
    #         yield scrapy.Request(url,self.parse)
    #         yield scrapy.Request(urls,self.parse)
    #         # yield scrapy.Request(urls,self.parse)
    # def parse(self, response):
    #     print(response.url)
