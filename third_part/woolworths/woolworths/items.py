import scrapy

class WoolworthsItem(scrapy.Item):
    breadcrumb = scrapy.Field()
    products = scrapy.Field()
