import scrapy
import json
from naveropenapi.items import NaveropenapiItem
class NavershoppingSpider(scrapy.Spider):
    name = 'navershopping'
    #allowed_domains = ['openapi.naver.com/v1/search']
    start_urls = ['https://openapi.naver.com/v1/search/shop.json?query=']

    def parse(self, response):
        print(response.text)
        data = json.loads(response.text)
        for item in data['items']:
            vo = NaveropenapiItem()
            vo['title'] = item['title']
            vo['link'] = item['link']
            vo['image'] =  item['image']
            vo['lprice'] =  item['lprice']
            vo['hprice']=  item['hprice']
            vo['mallName'] =  item['mallName']
            vo['productId'] =  item['productId']
            vo['productType'] =  item['productType']
            vo['brand'] =  item['brand']
            vo['maker'] =  item['maker']
            vo['category1'] =  item['category1']
            vo['category2'] =  item['category2']
            vo['category3'] =  item['category3']
            vo['category4'] =  item['category4']
            yield vo

    def start_requests(self):
        client_id='mBHQgcAf07hnOOkTs4qK'
        client_secret='rnqMZrshkU'
        header_params={'X-Naver-Client-Id':client_id,'X-Naver-Client-Secret':client_secret}
        query='perfume'
        for url in self.start_urls:
            yield scrapy.Request(url+query,headers=header_params)
