# -*- coding: utf-8 -*-
import scrapy
from catchDemoJd.items import CatchdemojdItem
from scrapy_splash import SplashRequest


class JdspiderSpider(scrapy.Spider):
    name = 'jdSpider'
    allowed_domains = ['product.suning.com']
    start_urls = ['https://product.suning.com/0000000000/10597840419.html']

    # 重写请求方法
    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url, args={'timeout': 8, 'images': 0})

    def parse(self, response):
        item = CatchdemojdItem()
        item['good'] = response.xpath('//*[@id="itemDisplayName"]/text()').extract_first()
        price = response.xpath('//*[@id="mainPrice"]/dl[1]/dd/span[@class="mainprice"]//text()').extract()[1]
        item['price'] = price[0: 5]
        item['shop'] = response.xpath('//div[@class="header-shop-inline"]/a/text()').extract_first()
        yield item
