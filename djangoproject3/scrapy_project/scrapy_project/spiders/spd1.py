import scrapy
from ..items import ScrapyProjectItem

class QuotesSpider(scrapy.Spider):

    start_urls = ['https://cxsecurity.com/wlb/']

    name = "spd1"

    def parse(self, response, **kwargs):
        

        links = response.css('div.col-md-7 > h6 > a::attr(href)').getall()
        for link in links:
            yield scrapy.Request(url=link,callback=self.parse_link)
        
    def parse_link(self, response):
        item = ScrapyProjectItem()
        # print(response.url)   
        item["title"] = response.css("center h4 b::text").get()
        item["date"] = response.css("div.col-xs-12 div.well-sm b::text").get()
        item["risk"] = response.css("div > b > span::text").get()
        item["cve"] = response.css("div:nth-child(6) > div > b::text").get()
        item["cwe"] = response.css("div:nth-child(7) > div > b::text").get()
        yield item

