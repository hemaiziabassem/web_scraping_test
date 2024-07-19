import scrapy

class IcedTeasSpider(scrapy.Spider):
    name = 'iced_teas'
    start_urls = ['https://www.woolworths.com.au/shop/browse/drinks/cordials-juices-iced-teas/iced-teas']

    def parse(self, response):
        # Extract breadcrumb
        breadcrumb = response.css('nav.breadcrumbs a::text').getall()
        breadcrumb = [b.strip() for b in breadcrumb]  # Clean whitespace
        self.log(f'Breadcrumbs: {breadcrumb}')  # Debug log

        # Extract product names
        products = response.css('a.product-tile__title::text').getall()
        products = [p.strip() for p in products]  # Clean whitespace
        self.log(f'Products: {products}')  # Debug log

        yield {
            'breadcrumb': breadcrumb,
            'products': products,
        }
