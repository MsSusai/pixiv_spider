# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from scrapy.pipelines.images import ImagesPipeline
from scrapy import Request


class PixivSpiderPipeline:
    def process_item(self, item, spider):
        # print(item)
        return item


class DownloadImagesPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        for imgUrl in item['imageUrl']:
            yield Request(imgUrl, meta={'imageName': item['imageName']})

    def file_path(self, request, response=None, info=None, *, item=None):
        name = request.meta['imageName'] + '.jpg'
        return name
