# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyProjectItem(scrapy.Item):
    title = scrapy.Field()
    date = scrapy.Field()
    risk = scrapy.Field()
    cve = scrapy.Field()
    cwe = scrapy.Field()
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
