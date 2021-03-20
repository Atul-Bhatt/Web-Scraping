import scrapy

# TODO: create a class that will inherit Spider class of scrapy


class QuotesSpider(scrapy.Spider):
    # name identifies the Spider. It must be unique within a project
    # you can't use the same for a different Spider.
    name = "quotes"

    # TODO: state urls that you want to scrape and iterate a callback
    #  function
    # def start_requests(self):
    #     urls = [
    #         "http://quotes.toscrape.com/page/1"
    #         # "http://quotes.toscrape.com/page/2"
    #     ]
    #     for url in urls:
    #         yield scrapy.Request(url=url, callback=self.parse)

    # TODO: Use start_urls if you don't want to implement start_requests()
    start_urls = [
        "http://quotes.toscrape.com/page/1/",
        "http://quotes.toscrape.com/page/2/"
    ]

    # TODO: define the parse function that will scrape the web
    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').get().strip("\u201d").strip("\u201c"),
                'author': quote.css('small.author::text').get(),
                'tags': quote.css('div.tags a.tag::text').getall()
            }
