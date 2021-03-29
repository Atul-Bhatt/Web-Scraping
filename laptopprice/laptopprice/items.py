# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Laptop(scrapy.Item):
    Model = scrapy.Field()
    RAM = scrapy.Field()
    Processor = scrapy.Field()
    OS = scrapy.Field()
