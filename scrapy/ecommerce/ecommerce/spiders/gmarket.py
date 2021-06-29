import scrapy
from ecommerce.items import EcommerceItem

class GmarketSpider(scrapy.Spider):
    name = 'gmarket'
    #allowed_domains = ['www.gmarket.co.kr']
    start_urls = ['http://corners.gmarket.co.kr/Bestsellers']

    def parse(self, response):
        #print(response.text)
        print(response.url)
        titles = response.css('div.best-list li a::text').getall()
        prices = response.css('div.item_price > div.s-price > strong > span > span::text').getall()
        for indx, title in enumerate(titles):
            item = EcommerceItem()
            item['title'] = title
            item['price'] = prices[indx].strip().replace("원","").replace(",","")
            yield item

