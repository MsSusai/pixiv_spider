# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html
class Proxy(object):
    # 设置代理
    def process_request(self, request, spider):
        request.meta['proxy'] = 'https://127.0.0.1:10809'
