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
            names = ["tite", "tags", "url"]
            writer = csv.writer(csvfile, dialect="excel")
            writer.writerow([item['title'][0], item['tags'], item['url'][0]])


class PhotosPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        yield scrapy.Request(item['photos'][0])
        # if item['photos']:
        #     for img_url in item['photos']:
        #         try:
        #             yield scrapy.Request(img_url)
        #         except Exception as e:
        #             print(e)

    def item_completed(self, results, item, info):
        print()
        if results:
            item['photos'] = [itm[1] for itm in results if itm[0]]
        return item
