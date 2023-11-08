# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import TakeFirst


class UnsplashItem(scrapy.Item):
    # define the fields for your item here like:
    url = scrapy.Field(output_processor=TakeFirst())
    title = scrapy.Field(output_processor=TakeFirst())
    tags = scrapy.Field()
    photos = scrapy.Field(output_processor=TakeFirst())
