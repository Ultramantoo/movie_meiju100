# -*- coding: utf-8 -*-
import scrapy
from movie.items import MovieItem


class MeijuSpider(scrapy.Spider):
    name = 'meiju'
    allowed_domains = ['meijutt.com']
    start_urls = ['https://www.meijutt.com/new100.html']

    def parse(self, response):
        movie = response.xpath(
            '//ul[contains(@class,"top-list") and contains(@class,"fn-clear")]/li')  # 用xpath对网页返回的response对象进行解析
        for each_movie in movie:
            item = MovieItem()  # 实例出item对象
            item['name'] = each_movie.xpath('./h5/a/@title').extract()[0]  # 提起name字段
            item["classification"] = each_movie.xpath('./span[2]/text()').extract_first()  # 提取classification字段
            item["state"] = each_movie.xpath('./span[1]/font[1]/text()').extract_first()
            yield item  # 返回item，并交由pipeline管道处理
