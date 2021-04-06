# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class Laptop(Item):
    Model = Field()
    RAM = Field()
    Processor = Field()
    OS = Field()
    Memory = Field()
    Display = Field()
    # last_updated = Field(serializer=str)
