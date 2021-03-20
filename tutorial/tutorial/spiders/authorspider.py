# scrape author information
import scrapy


class AuthorSpider(scrapy.Spider):
    # Name of the spider
    name = 'author'

    start_urls = [
        "http://quotes.toscrape.com/page/1"
    ]

    def parse(self, response):
        author_page_links = response.css('.author + a')
        yield from response.follow_all(author_page_links, self.parse_author)

        pagination_links = response.css('li.next a')
        yield from response.follow_all(pagination_links, self.parse)

    def parse_author(self, response):
        def extract_with_css(query):
            return response.css(query).get(default='').strip()

        yield {
            'Name': extract_with_css('h3.author-title::text'),
            'Birthdate': extract_with_css('.author-born-date::text'),
            'Bio': extract_with_css('.author-description::text')
        }
