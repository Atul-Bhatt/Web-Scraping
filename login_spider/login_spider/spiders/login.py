# -*- coding: utf-8 -*-
from scrapy import Spider
from scrapy.http import FormRequest
from scrapy.utils.response import open_in_browser


class QuotesSpider(Spider):
    name = 'login'
    start_urls = ('https://scrapingclub.com/exercise/basic_login/',)

    def parse(self, response):
        token = response.xpath(
            '//*[@name="csrfmiddlewaretoken"]/@value').extract_first()
        return FormRequest.from_response(response,
                                         formdata={'csrf_token': token,
                                                   'name': 'scrapingclub',
                                                   'password': 'scrapingclub'},
                                         callback=self.scrape_pages)

    def scrape_pages(self, response):
        open_in_browser(response)

        # Complete your code here to scrape the pages that you are redirected to after logging in

        # ....
        # ....
