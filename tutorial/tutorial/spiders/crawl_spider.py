# Using LinkExtractor and Rule objects

import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

# TODO: create a subclass of CrawlSpider


class MySpider(CrawlSpider):
    # Name of the spider
    name = 'practiceSpider'
    allowed_domains = ["example.com"]
    start_urls = ["http://example.com"]

    # TODO: define a rule
    rule = (
        # Extract links matching 'category.php' (but not matching subsection.php)
        # and follow links from them since no callback means follow=True by default
        Rule(LinkExtractor(allow=('category\.php',), deny=('subsectoin\.php',))),
        # Extract links matching item.php and parse them using spider's parse_item method
        Rule(LinkExtractor(allow=('item.php',)), callback='parse_item')
    )

    def parse_item(self, response):
        self.logger.info(f"Hi, this is an item page {response.url}")
        item = scrapy.Item()
        item['id'] = response.xpath(
            '//td[@id="item_id"]/text()').re(r'ID: (\d+)')
        item['name'] = response.xpath('//td[@id="item_name"]/text()').get()
        item['description'] = response.xpath(
            '//td[@id="item_description"]/text()').get()
        item['link_text'] = response.meta('link_text').get()
        url = response.xpath('//td[@id="additional_data"]/@href').get()
        return response.followo(url, self.parse_additional_page, cb_kwargs=dict(item=item))

    def parse_additional_page(self, response, item):
        item['additional_data'] = response.xpath(
            '//p[@id="additional_data"]/text()').get()
        return item
