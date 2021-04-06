import scrapy
from laptopprice.items import Laptop
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class LaptopsSpider(CrawlSpider):
    name = 'laptops'
    allowed_domains = ['flipkart.com']
    start_urls = [
        'https://www.flipkart.com/search?q=laptops&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off']

    custom_settings = {
        'FEED_URI': 'laptops_new.json',
        'FEED_FORMAT': 'json'
    }

    rules = [
        Rule(LinkExtractor(restrict_xpaths=("//a[@class='_1LKTO3']")),
             callback='parse', follow=True)
    ]

    def parse(self, response):
        laptop = Laptop()

        for x in response.xpath("//div[@class='_1AtVbE col-12-12']"):
            model = x.css('div._4rR01T::text').get()
            if model is not None:
                # yield {
                #     'Model': model,
                #     'Processor': x.xpath('.//li[@class="rgWa7D"][1]/text()').get(),
                #     'RAM': x.xpath('.//li[@class="rgWa7D"][2]/text()').get(),
                #     'OS': x.xpath('.//li[@class="rgWa7D"][3]/text()').get(),
                #     'Memory': x.xpath('.//li[@class="rgWa7D"][4]/text()').get(),
                #     'Display': x.xpath('.//li[@class="rgWa7D"][5]/text()').get()
                # }
                laptop['Model'] = model
                laptop['RAM'] = x.xpath(
                    './/li[@class="rgWa7D"][2]/text()').get()
                laptop['Processor'] = x.xpath(
                    './/li[@class="rgWa7D"][1]/text()').get()
                laptop['OS'] = x.xpath(
                    './/li[@class="rgWa7D"][3]/text()').get()
                laptop['Memory'] = x.xpath(
                    './/li[@class="rgWa7D"][4]/text()').get()
                laptop['Display'] = x.xpath(
                    './/li[@class="rgWa7D"][5]/text()').get()

        # yield from response.follow_all(css='a._1LKTO3', callback=self.parse)

        yield laptop
