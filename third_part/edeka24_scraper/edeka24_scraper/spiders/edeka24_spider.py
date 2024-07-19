import scrapy
from items import Edeka24ScraperItem

class Edeka24Spider(scrapy.Spider):
    name = "edeka24"
    start_urls = [
        'https://www.edeka24.de/Lebensmittel/Suess-Salzig/Schokoriegel/'
    ]

    def parse(self, response):
        # Extract product names, prices, and URLs
        for product in response.css('div.product-details'):
            item = Edeka24ScraperItem()
            item['name'] = product.css('a.title h2::text').get()
            item['price'] = product.css('div.price::text').get().strip()
            item['url'] = response.urljoin(product.css('a.title::attr(href)').get())
            yield item
        
        # Follow pagination links
        next_page = response.css('a.next::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
