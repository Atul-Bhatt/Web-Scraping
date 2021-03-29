import scrapy
from laptopprice.items import Laptop


class LaptopsSpider(scrapy.Spider):
    name = 'laptops'
    allowed_domains = ['flipkart.com']
    start_urls = [
        'https://www.flipkart.com/search?q=laptops&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off']

    # custom_settings = {
    #     'FEED_URI': 'laptops.json',
    #     'FEED_FORMAT': 'json'
    # }

    def parse(self, response):
        # laptop = Laptop()

        for x in response.xpath("//div[@class='_1AtVbE col-12-12']"):
            model = x.css('div._4rR01T::text').get()
            if model is not None:
                yield {
                    'Model': model,
                    'Processor': x.xpath('.//li[@class="rgWa7D"][1]/text()').get(),
                    'RAM': x.xpath('.//li[@class="rgWa7D"][2]/text()').get(),
                    'OS': x.xpath('.//li[@class="rgWa7D"][3]/text()').get(),
                    'Memory': x.xpath('.//li[@class="rgWa7D"][4]/text()').get(),
                    'Display': x.xpath('.//li[@class="rgWa7D"][5]/text()').get()
                }
            # laptop['Model'] = x.css('div._4rR01T::text').get()
            # laptop['RAM'] = '4GB'
            # print(x.css('div._4rR01T::text').get())
            # laptop['Model'] = x.xpath(
            #     ".//div[@class='_4rR01T']/text()").get()
        yield from response.follow_all(css='a._1LKTO3', callback=self.parse)
