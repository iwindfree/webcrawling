# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class NaveropenapiItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    image = scrapy.Field()
    lprice = scrapy.Field()
    hprice = scrapy.Field()
    mallName = scrapy.Field()
    productId = scrapy.Field()
    productType = scrapy.Field()
    brand = scrapy.Field()
    maker = scrapy.Field()
    category1 = scrapy.Field()
    category2 = scrapy.Field()
    category3 = scrapy.Field()
    category4 = scrapy.Field()
