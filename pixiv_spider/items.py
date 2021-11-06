# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PixivSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    imageName = scrapy.Field()
    imageUrl = scrapy.Field()
    imagePid = scrapy.Field()
    imageNum = scrapy.Field()
    image = scrapy.Field()
    pass
