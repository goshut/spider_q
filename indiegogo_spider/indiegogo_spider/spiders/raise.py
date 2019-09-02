# -*- coding: utf-8 -*-
import scrapy


class RaiseSpider(scrapy.Spider):
    name = 'raise'
    allowed_domains = ['www.indiegogo.com']
    start_urls = ['http://www.indiegogo.com/']

    def parse(self, response):
        pass
