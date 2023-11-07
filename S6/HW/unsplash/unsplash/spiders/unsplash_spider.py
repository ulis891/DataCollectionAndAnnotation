# -*- coding: utf-8 -*-
import requests
import scrapy
from scrapy.loader import ItemLoader
from scrapy.http import HtmlResponse

from S6.HW.unsplash.unsplash.items import UnsplashItem


class UnsplashSpiderSpider(scrapy.Spider):
    name = 'unsplash_spider'
    allowed_domains = ['unsplash.com']

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.start_urls = [f"https://unsplash.com/s/photos/{kwargs.get('query')}"]

    def parse(self, response: HtmlResponse):
        links = response.xpath("//a[@itemprop='contentUrl']/@href").getall()
        for link in links:
            yield response.follow(link, callback=self.parse_photo)

    def parse_photo(self, response: HtmlResponse):
        loader = ItemLoader(item=UnsplashItem(), response=response)
        loader.add_xpath('title', '//h1/text()')
        loader.add_xpath('tags', '//div[@class="MbPKr M5vdR"]//div[@class="VZRk3 rLPoM"]//a/text()')
        loader.add_value('url', response.url)
        loader.add_xpath('photos', "//div[@class='MorZF']/img/@src")
        yield loader.load_item()
