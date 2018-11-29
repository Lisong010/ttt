#-*- encoding:utf-8 -*-
import scrapy
import time
import re

class JingDong(scrapy.Spider):
    name='jingdon'
    allowed_domains=[]
    # start_urls=['https://search.jd.com/Search?keyword=%E5%9C%B0%E7%93%9C&enc=utf-8&wq=di%27gua&pvid=ea355a0c2fd04020a60bf0e880e54a0e']

    def start_requests(self):
        for i in range(1,2):
            url='https://search.jd.com/Search?keyword=%E5%9C%B0%E7%93%9C&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=di%27gua&stock=1&page='+str(i)+'&s=59&click=0'
            if i==2:
                continue
            yield scrapy.Request(url,self.parse)

    def parse(self,response):
        hrefs=re.findall('id="J_AD_(.*?)"',response.text)
        for href in hrefs:
            url='https://item.jd.com/'+str(href)+'.html'
            # print(url)# 30个链接
            yield scrapy.Request(url,self.left)

    def left(self,response):
        title = response.xpath("//div[@class='sku-name']/text()").extract()[0].strip()
        print(title)
        # price = response.xpath("//span[@class='price J-p-4087121']/text()").extract()
        # print(price)
        # t=round(time.time(),5)
        # url='https://search.jd.com/s_new.php?keyword=%E5%9C%B0%E7%93%9C&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=di%27gua&stock=1&page=2&s=29&scrolling=y&log_id='+str(t)
        # print(url)
        # yield scrapy.Request(url=url,callback=self.right)
    #
    # def right(self,response):
    #     title = response.xpath("//div[@class='sku-name']/text()").extract()[0].strip()
    #     print(title)