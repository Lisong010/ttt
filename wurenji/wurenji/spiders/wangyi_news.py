# -*- coding: utf-8 -*-
from scrapy.selector import Selector
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
import re


class WangYiSpider(CrawlSpider):
    name = 'wang'
    allowed_domains=[]
    start_urls = ['http://tech.163.com/gd/']

    rules = (
        Rule(LinkExtractor(allow="http://tech.163.com/special/gd2016_0\d+/"),follow=True),
        Rule(LinkExtractor(allow="http://tech.163.com/(.*?).html",restrict_css="h3.bigsize a"),
             callback="parse_item",follow=False)
    )

    def parse_item(self, response):
        sel = Selector(response)
        try:
            if sel.xpath("//div[@id='epContentLeft']/h1/text()"):
                title = sel.xpath("//div[@id='epContentLeft']/h1/text()").extract_first()
                print("标题："+title)
            else:
                raise Exception('title is null')
            if sel.xpath("//div[@class='post_body']/div[@id='endText']/p/text()"):
                article =sel.xpath("//div[@class='post_body']/div[@id='endText']/p/text()").extract()
                for art in article:
                    print(art)
            else:
                article=''
            if sel.xpath("//div[@id='epContentLeft']/div[@class='post_time_source']/text()"):
                time=sel.xpath("//div[@id='epContentLeft']/div[@class='post_time_source']/text()").extract_first()
                print("时间："+time[:36].strip())
            else:
                raise Exception('time is none')
            if sel.xpath("//div[@class='post_time_source']/a[@id='ne_article_source']/text()"):
                laiyuan =sel.xpath("//div[@class='post_time_source']/a[@id='ne_article_source']/text()").extract_first()
                print("来源："+laiyuan)
            else:
                laiyuan=''
            if sel.xpath("//div[@class='ep-source cDGray']/span[@class='ep-editor']/text()"):
                zuozhe = sel.xpath("//div[@class='ep-source cDGray']/span[@class='ep-editor']/text()").extract_first()
                print("作者：" + zuozhe)
            else:
                zuozhe=''
            if re.findall('<meta name="keywords" content="(.*?)"/>',response.text):
                keyword = re.findall('<meta name="keywords" content="(.*?)"/>',response.text)[0]
                print("关键字："+keyword)
            else:
                keyword=''
            if re.findall('<meta name="description" content="(.*?)"/>',response.text):
                daodu = re.findall('<meta name="description" content="(.*?)"/>',response.text)[0]
                print("导读："+daodu)
            else:
                daodu=''
        except:
            pass
