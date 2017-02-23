
from scrapy.contrib.downloadermiddleware.useragent import UserAgentMiddleware

class CustomMiddleware(UserAgentMiddleware):
    def process_request(self, request, spider):
        userAgent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
        request.headers.setdefault('User-Agent',userAgent)

class CustomProxy(object):
    def process_request(self,request,spider):
        request.meta['proxy'] = 'http://112.25.44.35:55336'