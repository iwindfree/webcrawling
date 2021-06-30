import scrapy
from ecommerce.items import CategoryItem

class GmarketCategoryAllSpider(scrapy.Spider):
    name = 'gmarket_category_all'
    #allowed_domains = ['http://corners.gmarket.co.kr/Bestsellers']
    #start_urls = ['http://corners.gmarket.co.kr/Bestsellers/']
    def start_requests(self):
        yield scrapy.Request(url='http://corners.gmarket.co.kr/Bestsellers/',callback=self.parse)
        #yield scrapy.Request(url='http://corners.gmarket.co.kr/Bestsellers?viewType=G&groupCode=G01',callback=self.parse1)

    def parse(self, response):
        category_links = response.css('div.gbest-cate ul.by-group li a::attr(href)').getall()
        category_names = response.css('div.gbest-cate ul.by-group li a::text').getall()

        for indx, category_link in enumerate(category_links):
            yield scrapy.Request(url='http://corners.gmarket.co.kr' + category_link,
                                 callback=self.parseItems,
                                 meta={'main_category_name':category_names[indx],'sub_category_name':'All'}
                                 )

        for indx, category_link in enumerate(category_links):
            yield scrapy.Request(url='http://corners.gmarket.co.kr' + category_link,
                                 callback=self.parsesubcategory,
                                 meta={'main_category_name': category_names[indx]}
                                 )
            #print('http://corners.gmarket.co.kr/'+ category_link,':', category_names[indx])


    def parseItems(self, response):
        best_items = response.css('div.best-list')
        item_list = best_items[1].css('li')
        for indx, item in enumerate(item_list):
            ranking = indx +1
            title = item.css('a.itemname::text').get()
            original_price = item.css('div.o-price span span::text').get()
            discount_price = item.css('div.s-price strong span span::text').get()
            discount_pct = item.css('div.s-price em::text').get()
            if original_price == None:
                original_price = discount_price
            if discount_pct == None:
                discount_pct = "0%"
            print(ranking, ' ', title, ' ', original_price, ' ', discount_price, ' ', discount_pct)

            discount_pct = discount_pct.replace("%","")
            original_price = original_price.replace("원","").replace(",","")
            discount_price = discount_price.replace("원", "").replace(",","")

            item = CategoryItem()
            item['category_name'] = response.meta['main_category_name']
            item['sub_category_name'] = response.meta['sub_category_name']
            item['ranking'] = ranking
            item['ori_price'] = original_price
            item['dis_price'] = discount_price
            item['discount_pct'] = discount_pct
            item['title'] = title
            yield  item




    def parsesubcategory(self,response):
        print( " SUB->" , response.meta['main_category_name']    )
        subcategory_links = response.css('div.navi.group > ul > li > a::attr(href)').getall()
        subcategory_names = response.css('div.navi.group > ul > li > a::text').getall()
        for indx, subcategory in enumerate(subcategory_links):
            print('http://corners.gmarket.co.kr/'+ subcategory,' ', subcategory_names[indx])
            yield scrapy.Request(url='http://corners.gmarket.co.kr' + subcategory,
                                 callback=self.parseItems,
                                 meta={'main_category_name': response.meta['main_category_name'],
                                       'sub_category_name':subcategory_names[indx]
                                       }
                                 )

    """
    def parse1(self, response):
        print('call parse1')
    """