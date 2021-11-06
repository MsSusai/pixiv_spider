import scrapy
from pixiv_spider.items import PixivSpiderItem


class PixivSpider(scrapy.Spider):
    name = 'pixiv'
    allowed_domains = ['www.pixiv.net']
    start_urls = ['https://www.pixiv.net/ajax/user/3718340/profile/all?lang=zh']

    def parse(self, response):
        json = response.json()
        imageIds = json['body']['illusts'].keys()
        for imageId in imageIds:
            item = PixivSpiderItem()
            # print(imageId)
            imgUrl = 'https://www.pixiv.net/ajax/illust/' + str(imageId)
            request = scrapy.Request(imgUrl, callback=self.parse_imgName)
            request.meta['item'] = item
            yield request

    '''
    yield request是将这个请求任务放到downloader中，请求成功返回response对象交给callback函数处理。
    在返回response之前，for循环继续运行将request添加到任务中。这时imgUrl就已经改变了
    不添加yield的话，parse的for会一直等（阻塞）scrapy.Request(url,callback=self.parse_imgName)这个请求返回response，然后交给parse_imgName处理。处理完之后再执行下一个for
    '''

    def parse_imgName(self, response):  # 处理每个pid，添加图片名称
        item = response.meta['item']
        json = response.json()
        imageUrlList = [json['body']['urls']['regular']]
        item['imageUrl'] = imageUrlList

        '''
        共有五种图片清晰度下载选项,根据自已需要修改
        mini
        thumb
        small
        regular
        original
        '''

        item['imageName'] = json['body']['illustTitle']
        # print(item)
        yield item
