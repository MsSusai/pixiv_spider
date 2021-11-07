# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from scrapy.pipelines.images import ImagesPipeline
from scrapy import Request
from pixiv_spider.settings import IMAGES_STORE as image_store
import os

i = 1


class PixivSpiderPipeline:

    def process_item(self, item, spider):
        # for imgUrl in item['imageUrl']:
        #     print(imgUrl)
        return item


class DownloadImagesPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        global i
        for imgUrl in item['imageUrl']:
            print("正在处理第{}张".format(i))
            i += 1
            yield Request(imgUrl)

    def item_completed(self, results, item, info):
        # if len(item['imageNum']) > 1:
        #     os.rename(image_store + '/' + results[0][1]['path'],
        #               image_store + '/' + item['imageName'] + '_p' + str(item['imageNum'].pop(0)) + '.jpg')
        # else:
        os.rename(image_store + '/' + results[0][1]['path'],
                  image_store + '/' + item['imageName'] + '.jpg')

    def __del__(self):
        # 完成后删除full目录
        os.removedirs(image_store + '/' + 'full')
