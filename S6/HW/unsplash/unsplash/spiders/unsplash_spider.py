# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from scrapy.http import HtmlResponse

from DataCollectionAndAnnotation.S6.HW.unsplash.unsplash.items import UnsplashItem


class UnsplashSpiderSpider(scrapy.Spider):
    name = 'unsplash_spider'
    allowed_domains = ['www.unscplash.com']

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.start_urls = [f"https://unsplash.com/s/photos/{kwargs.get('query')}"]

    def parse(self, response: HtmlResponse):
        links = response.xpath("//a[@itemprop='contentUrl']")
        for link in links:
            print(link)
            yield response.follow(link, callback=self.parse_photo)

    def parse_photo(self, response: HtmlResponse):
        print('23424234')
        url = response.url
        title = response.xpath("//h1/text()").get()
        yield UnsplashItem(url=url, title=title)

        # loader = ItemLoader(item=Book24Item(), response=response)
        # loader.add_xpath('name', '//h1/text()')
        # loader.add_xpath('price', "//span[@class='app-price product-sidebar-price__price']/text()")
        # loader.add_value('url', response.url)
        # loader.add_xpath('photos', "//picture[@class='product-poster__main-picture']/source[1]/@srcset |"
        #                            "//picture[@class='product-poster__main-picture']/source[1]/@data-srcset")
        # loader = ItemLoader(item=UnsplashItem(), response=response)
        # loader.add_value('url', response.url)
        # yield loader.load_item()
