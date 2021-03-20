# get the quotes using tag provided from command line
import scrapy


class TagSpider(scrapy.Spider):
    name = 'tagSpider'

    def start_requests(self):
        url = "http://quotes.toscrape.com/"

        tag = getattr(self, 'tag', None)
        if tag is not None:
            url = url + 'tag/' + tag
        yield scrapy.Request(url, meta={
            'dont_redirect': True,
            'handle_httpstatus_list': [308, 404]
        }, callback=self.parse)

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': response.css('span.text::text').get(),
                'author': response.css('small.author::text').get()
            }

        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
