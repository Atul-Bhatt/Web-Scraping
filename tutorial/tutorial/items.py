# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class Product(Item):
    name = Field()
    price = Field()
    stock = Field()
    tags = Field()
    last_updated = Field(serializer=str)
