# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class CatchdemojdPipeline(object):
    def process_item(self, item, spider):
        print(item)
        # with open('jdIponexs.txt', 'a') as file:
        # file.write('标题：' + item['good'] + '\n' + '店铺名称：' + item['shop'] + '\n' + item['priceFrom'] + ':' + item[
        #     'price'] + '\n\n')
