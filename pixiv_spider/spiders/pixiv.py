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
            item['imagePid'] = imageId
            imgUrl = 'https://www.pixiv.net/ajax/illust/' + str(imageId) + '/pages'  # 这个链接的json存放着每一个图片的下载链接和标题
            request = scrapy.Request(imgUrl, callback=self.parse_imgUrl)
            request.meta['item'] = item
            yield request

    '''
    yield request是将这个请求任务放到downloader中，请求成功返回response对象交给callback函数处理。
    在返回response之前，for循环继续运行将request添加到任务中。这时imgUrl就已经改变了
    不添加yield的话，parse的for会一直等（阻塞）scrapy.Request(url,callback=self.parse_imgName)这个请求返回response，然后交给parse_imgName处理。处理完之后再执行下一个for
    '''

    def parse_imgUrl(self, response):  # 处理每个pid，添加图片名称
        json = response.json()
        item = response.meta['item']
        imageUrlList = []  # url必须是个列表才能被请求
        imageNumList = []  # 计数有几个子url链接
        for url in json['body']:
            imageUrlList.append(url['urls']['regular'])
        item['imageUrl'] = imageUrlList

        '''
        共有五种图片清晰度下载选项,可以根据自已需要修改
        mini
        thumb
        small
        regular
        original
        '''
        for i in range(len(imageUrlList)):
            imageNumList.append(i)
        item['imageNum'] = imageNumList

        imgNameUrl = 'https://www.pixiv.net/ajax/illust/' + str(item['imagePid'])
        request = scrapy.Request(imgNameUrl, callback=self.parse_imgName)
        request.meta['item'] = item
        yield request

    def parse_imgName(self, response):
        item = response.meta['item']
        json = response.json()
        item['imageName'] = json['body']['illustTitle']
        # # print(item)
        yield item
