import scrapy
from ..items import Tablet

class AmazonSpider(scrapy.Spider):
    name = 'amazon_spider'
    
     # How many pages you want to scrape
    no_of_pages = 10

    # Headers to fix 503 service unavailable error
    # Spoof headers to force servers to think that request coming from browser ;)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}

    def start_requests(self):
        # starting urls for scraping
        urls = ["https://www.amazon.com/s?k=tablet&i=electronics&ref=nb_sb_noss_1"]

        for url in urls: yield scrapy.Request(url = url, callback = self.parse, headers = self.headers)

   