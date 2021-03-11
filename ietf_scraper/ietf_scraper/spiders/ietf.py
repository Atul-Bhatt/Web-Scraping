import scrapy

'''
We can run the spider by using runspider function of scrapy
scrapy runspider ietf.py

/html/body/div/h1
//h1                            Select any header
//div/h1                        Select headers which are immediate child of div
//div//h1                       Select headers which are anywhere inside of div
//span[@class="title"]          Select span which have class title
//span[@class="title"]/@id      Select value of the id attribute of the span which has class title
//span[@class="title"]/text()   will return result in text format.
'''


class IetfSpider(scrapy.Spider):
    name = 'ietf'
    allowed_domains = ['pythonscraping.com']
    start_urls = ['http://pythonscraping.com/linkedin/ietf.html']

    def parse(self, response):
        # title = response.css('span.title::text').get()
        # title = response.xpath('//span[@class="title"]/text()').get()
        title = response.xpath(
            '//div[@class="content"]/span[3]').get()
        return {"title": title}
