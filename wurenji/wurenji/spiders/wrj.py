# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
from ..items import WurenjiItem


class Wrj(CrawlSpider):
    name = 'wrj'
    allowed_domains = []
    start_urls = ['http://www.81uav.cn/uav-news/4.html']
    rules=(
        Rule(LinkExtractor(allow='http://www.81uav.cn/uav-news/4_\d+.html', ),follow=True),
        Rule(LinkExtractor(allow='http://www.81uav.cn/uav-news/\d{6}/\d{2}/\d+.html',restrict_css='div.news_left a'),
             callback='parse1',follow=False),
    )
    def parse1(self, response):
        # print(response.url)
        # item=WurenjiItem()
        sel=Selector(response)
        try:
            if sel.xpath('//h1/text()').extract_first():
                title=sel.xpath('//h1/text()').extract_first()
                print('标题：'+title)
            else:
                title=''
                print(response.url)
                raise Exception('title in null')
                # item['title'] = title
            if sel.css("div.info::text").re("\d{4}-\d{2}-\d{2}"):
                date = sel.css("div.info::text").re("\d{4}-\d{2}-\d{2}")[0]
                print('发布日期：' + date)
            else:
                date = ''
                raise Exception('date is null')
            # item['date']=date
            if sel.css('div.info::text').re('\w+')[5]:
                laiyuan=sel.css('div.info::text').re('\w+')[5]
                print('来源：'+laiyuan)
            else:
                laiyuan=''
                # item['laiyuan'] = laiyuan
            if sel.css('div.info::text').re('\w+')[7]:
                zuozhe=sel.css('div.info::text').re('\w+')[7]
                print('作者：'+zuozhe)
            else:
                zuozhe=''
                # item['zuozhe'] = zuozhe

            if sel.xpath("//div[@id='content']//p/text()").extract():
                article=sel.xpath("//div[@id='content']//p/text()").extract()
                for art in article:
                    print(art)
                    # item['article'] = art
            else:
                print()
            if sel.xpath("//p/img/@src").extract():
                image=sel.xpath("//p/img/@src").extract()
                for ima in image:
                    print(ima)
                    # item['image'] = ima
            else:
                print()
        except:
            pass
        # yield item

