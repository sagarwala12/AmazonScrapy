# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Tablet(scrapy.Item):
    title = scrapy.Field()
    brand = scrapy.Field()
    rating = scrapy.Field()
    price = scrapy.Field()
    colour = scrapy.Field()
    instock = scrapy.Field()
    reviews = scrapy.Field()
    description = scrapy.Field()
