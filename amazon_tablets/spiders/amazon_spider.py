#-*- coding: utf-8 -*-
import scrapy
from ..items import Tablet
import re

class AmazonSpider(scrapy.Spider):
    name = 'amazon_spider'
    #allowed_domains = ['amazon.com']
    #start_urls = ["https://www.amazon.com/s?k=tablet&i=electronics&ref=nb_sb_noss_1"]
     # How many pages to scrape
     #set to 1 for testing 
    no_of_pages = 400

    # Headers to fix 503 service unavailable error
    # User agent will make it look like request is coming from browser 
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}

    def start_requests(self):
        # starting urls for scraping
        urls = ["https://www.amazon.com/s?k=tablet&i=electronics&ref=nb_sb_noss_1"]

        for url in urls: yield scrapy.Request(url = url, callback = self.parse, headers = self.headers)

    def parse(self, response):

        self.no_of_pages -= 1

        tablets = response.xpath("//a[@class='a-link-normal a-text-normal']").xpath("@href").getall()

        # print(len(tablets))

        for tablet in tablets:
            final_url = response.urljoin(tablet)
            yield scrapy.Request(url=final_url, callback = self.parse_tablet, headers = self.headers)
            # break
            # print(final_url)

        # print(response.body)
        # title = response.xpath("//span[@class='a-size-medium a-color-base a-text-normal']//text()").getall()
        # title = response.css('span').getall()
        # print(title)
        
        if(self.no_of_pages > 0):
            next_page_url = response.xpath("//ul[@class='a-pagination']/li[@class='a-last']/a").xpath("@href").get()
            final_url = response.urljoin(next_page_url)
            yield scrapy.Request(url = final_url, callback = self.parse, headers = self.headers)

    def parse_tablet(self, response):
        title = response.xpath("//span[@id='productTitle']//text()").get() or response.xpath("//h1[@id='title']//text()").get()

        brand = response.xpath("//a[@id='bylineInfo']//text()").get() or "N/A"
        #print(brand)
        if brand.lower()[0] == 'b':
            brand = brand.split()[-1]
        else:
            brand = brand.split()[2]


        rating = response.xpath("//*[@id='acrPopover']/@title").get() or "N/A"
        # rating = response.xpath("//div[@id='averageCustomerReviews_feature_div']").xpath("//span[@class='a-icon-alt']//text()").get() or "N/A"
        # if rating[0] == 'P':
        #     rating = 'N/A'
        num_reviews = response.xpath("//div[@id='averageCustomerReviews_feature_div']").xpath("//span[@id='acrCustomerReviewText']//text()").get() or "N/A"

        #If original price striked out, select deal price, if deal price unavailable, select sale price, if all unavailable then N/A
        price = response.xpath("//span[@id='priceblock_ourprice']//text()").get() or response.xpath("//span[@id='priceblock_dealprice']//text()").get() or response.xpath("//span[@id='priceblock_saleprice']//text()").get() or 'N/A'


        #print(price)
        #if len(price) > 1: price = price[1].get()
        #elif len(price) == 1: price = price[0].get()
        #else : price = price.get()

        

        description_raw = response.xpath("//div[@id='feature-bullets']//li/span/text()").getall() or "N/A"
        


        description = []
        for description_temp in description_raw:
            description.append(description_temp.strip())

        print(title, brand, rating, price, num_reviews)
        # print(final_review)
        # print(reviews)
        # print(description)

        yield Tablet(title = title.strip(), brand = brand.strip(), rating = rating.strip(), num_reviews = num_reviews.strip(), price = price.strip(), description = description)


   