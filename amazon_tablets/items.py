# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Tablet(scrapy.Item):
    title = scrapy.Field()
    brand = scrapy.Field()
    rating = scrapy.Field()
    num_reviews = scrapy.Field()
    price = scrapy.Field()
    description = scrapy.Field()
