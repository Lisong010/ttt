# -*- coding: utf-8 -*-
import scrapy
import re


class WangyiSpider(scrapy.Spider):
    name = 'wangyi'
    allowed_domains = []
    start_urls = ['http://temp.163.com/special/00804KVA/cm_guonei.js?callback=data_callback']

    def parse(self, response):
        # print(response.text)
        hrefs=re.findall('"docurl":"(.*?)"',response.text)
        for href in hrefs:
            # print(href)
            yield scrapy.Request(href,self.parse1)
    def parse1(self,response):
        try:
            if response.xpath("//h1/text()").extract_first():
                title=response.xpath("//h1/text()").extract_first()
                print('标题：'+title)
            else:
                raise Exception('title is none')
            if response.xpath('//*[@id="epContentLeft"]/div[1]/text()').extract_first():
                date=response.xpath('//*[@id="epContentLeft"]/div[1]/text()').extract_first()
                # print(date.strip()[:20])
            else:
                raise Exception('date is none')
            laiyuan=response.xpath('//*[@id="ne_article_source"]/text()').extract_first()
            # print('来源：'+laiyuan)
            daodu=response.xpath('//*[@id="endText"]/p[1]/text()').extract_first()
            # print(daodu.strip())
            zuozhe=response.xpath('//*[@id="endText"]/div[2]/span[1]/text()').extract()
            # print(zuozhe)
            article=response.xpath('//*[@id="endText"]/p/text()').extract()
            # for art in article:
                # print(art)
            image=response.xpath("//div[@id='endText']/p[@class='f_center']/img/@src").extract()
            # for ima in image:
            #     print(ima)
            keyword=re.findall('<meta name="keywords" content="(.*?)"/>',response.text)[0]
            print('关键字：'+keyword)
        except:
            pass