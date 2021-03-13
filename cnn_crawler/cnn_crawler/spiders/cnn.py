import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from cnn_crawler.items import NewsArticle


class CnnSpider(CrawlSpider):
    name = 'cnn'
    allowed_domains = ['cnn.com']
    start_urls = ['https://www.cnn.com/india']

    rule = [
        Rule(LinkExtractor(), callback='parse_info', follow=True)
    ]

    def parse_info(self, response):
        article = NewsArticle()
        article['title'] = response.xpath('//h1/text()').get()
        return article
