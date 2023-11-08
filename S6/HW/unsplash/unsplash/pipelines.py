# -*- coding: utf-8 -*-
import csv
import os

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline
import scrapy


class UnsplashPipeline(object):
    def process_item(self, item, spider):
        with open(os.getcwd() + "/photos_info.csv", "a", encoding="UTF-8", newline="") as csvfile:
            writer = csv.writer(csvfile, dialect="excel")
            if os.stat("photos_info.csv").st_size == 0:
                writer.writerow(['title', 'tags', 'url'])
            writer.writerow([item['title'], item['tags'], item['url']])


class PhotosPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        yield scrapy.Request(item['photos'])


    def item_completed(self, results, item, info):
        if results:
            item['photos'] = [itm[1] for itm in results if itm[0]]
        return item
