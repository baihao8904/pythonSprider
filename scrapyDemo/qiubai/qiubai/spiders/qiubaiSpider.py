import scrapy
from qiubai.items import QiubaiItem


class QiubaispiderSpider(scrapy.Spider):
    name = "qiubaiSpider"
    allowed_domains = ["qiushibaike.com"]
    start_urls = []
    pages = 30
    for i in range(1,31):
        url = 'http://www.qiushibaike.com/hot/page/{}/'.format(str(i))
        start_urls.append(url)

    def parse(self, response):
        subSelector = response.xpath('//div[@class="article block untagged mb15" and @id]')
        items = []
        for sub in subSelector:
            item = QiubaiItem()
            item['author'] = sub.xpath('.//h2/text()').extract()[0]
            item['content'] = sub.xpath('.//div[@class="content"]/span/text()').extract()[0]
            item['img'] = sub.xpath('.//div[@class="thumb"]//img/@src').extract()
            item['funNum'] = sub.xpath('.//span[@class="stats-vote"]/i/text()').extract()[0]
            try:
                item['talkNum'] =sub.xpath('.//span[@class="stats-comments"]/a/i/text()').extract()[0]
            except:
                item['talkNum'] = 0
            items.append(item)
        return items
