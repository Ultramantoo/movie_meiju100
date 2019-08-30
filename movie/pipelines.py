# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class MoviePipeline(object):
    @staticmethod
    def process_item(item, spider):
        with open("myMovie.txt", "a") as fp:
            fp.write(item['name'] + '\t' + item['classification'] + '\t' + item['state'] + "\n")
        return item
