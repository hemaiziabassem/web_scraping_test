import scrapy


class Edeka24Spider(scrapy.Spider):
    name = "edeka24"
    allowed_domains = ["edeka24.com"]
    start_urls = ["https://edeka24.com"]

    def parse(self, response):
        pass
