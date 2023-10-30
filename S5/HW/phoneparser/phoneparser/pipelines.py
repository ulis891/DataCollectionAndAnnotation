# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import csv
import os

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class PhoneparserPipeline:

    def process_item(self, item, spider):
        with open(os.getcwd() + "/phones.csv", "a", encoding="UTF-8", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, dialect="excel")
            writer.writerow(item)

        return item
