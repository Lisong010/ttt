# -*- coding:utf-8 -*-

import scrapy

class Xinlang(scrapy.Spider):
    name='xinlang'
    allowed_domains=[]
    start_urls=['https://cre.mix.sina.com.cn/api/v3/get?callback=jQuery111205198039129401537_1543491654277&cateid=1z&cre=tianyi&mod=pctech&merge=3&statics=1&length=15&up=0&down=0&tm=1543491655&action=0']
    # def start_requests(self):
    #     for i in range(1,5):
    #         url='https://cre.mix.sina.com.cn/api/v3/get?callback=jQuery111205198039129401537_1543491654277&cateid=1z&cre=tianyi&mod=pctech&merge=3&statics=1&length=15&up='+str(i)+'&down=0&tm=1543491655&action='+str(i)
    #         yield scrapy.Request(url,self.parse)

    def parse(self, response):
        print(response.text)