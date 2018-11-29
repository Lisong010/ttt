# -*- coding: utf-8 -*-

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector


class KeJi(CrawlSpider):
    name = 'kjqy'
    allowed_domains = []
    start_urls = ['http://www.dayinhu.com/news/category/%E7%A7%91%E6%8A%80%E5%89%8D%E6%B2%BF']

    rules = (
        Rule(LinkExtractor(allow='http://www.dayinhu.com/news/category/%E7%A7%91%E6%8A%80%E5%89%8D%E6%B2%BF/page/\d+'),
             follow=True),
        Rule(LinkExtractor(allow='http://www.dayinhu.com/news/\d{6}.html', restrict_css='h1.entry-title a'),
             callback='parse_item', follow=False, )
    )

    def parse_item(self, response):
        # print(response.url)
        sel = Selector(response)
        try:
            if sel.xpath('//h1/text()').extract_first():
                title = sel.xpath('//h1/text()').extract_first()
                print('标题：' + title)
            else:
                raise Exception('title is null...')
            if sel.xpath('//*/footer/a[1]/time/text()').extract_first():
                date = sel.xpath('//*/footer/a[1]/time/text()').extract_first()
                print('发布时间：' + date)
            else:
                raise Exception('date is null...')
            if sel.xpath("//div[@class='entry-content']/p/text()").extract():
                laiyuan = sel.xpath("//div[@class='entry-content']/p/text()").extract()
                if '来源' in laiyuan[-1]:
                    print(laiyuan[-1])
                else:
                    laiyuan=''
            else:
                print(response.url)
            if sel.xpath('//div/p/text()').extract():
                article=sel.xpath('//div/p/text()').extract()
                for art in article[:-1]:
                    print(art)
            else:
                art=''
        except:
            pass
