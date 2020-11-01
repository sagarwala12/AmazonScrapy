# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
# from scrapy.exporters import CsvItemExporter

# class WriteItemPipeline(object):

#     def __init__(self):
#         self.filename = 'data.csv'

#     def open_spider(self, spider):
#         self.csvfile = open(self.filename, 'wb')
#         self.exporter = CsvItemExporter(self.csvfile)
#         self.exporter.start_exporting()

#     def close_spider(self, spider):
#         self.exporter.finish_exporting()
#         self.csvfile.close()

#     def process_item(self, item, spider):
#         self.exporter.export_item(item)
#         return item

from scrapy.exporters import JsonItemExporter

class WriteItemPipeline(object):
    def __init__(self):
        self.file = open("data2.json", 'wb')
        self.exporter = JsonItemExporter(self.file)#, encoding='utf-8', ensure_ascii=False)
        self.exporter.start_exporting()

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item