# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json


class WangyiPipeline:

    def open_spider(self, spider):
        if spider.name == 'job':
            self.file = open('wangyi.json', 'w')

    def process_item(self, item, spider):
        if spider.name == 'job':
            item = dict(item)

            str_data = json.dumps(item, ensure_ascii=False) + ',\n'

            self.file.write(str_data)

        return item

    def close_spider(self, spider):
        if spider.name == 'job':
            self.file.close()
