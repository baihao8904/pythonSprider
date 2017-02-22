# -*- coding: utf-8 -*-
import scrapy


class GuaziXaSpider(scrapy.Spider):
    name = "guazi_xa"
    allowed_domains = ["'guazi.com'"]
    start_urls = ('https://www.guazi.com/xa/')

    def parse(self, response):
        bbsExtra = GsExtractor()
        # 设置xslt抓取规则
        bbsExtra.setXsltFromAPI("31d24931e043e2d5364d03b8ff9cc77e", "guazi")
        # 调用extract方法提取所需内容
        result = bbsExtra.extractHTML(response.body)

        # 打印采集结果
        print(str(result).encode('gbk','ignore').decode('gbk'))
        # 保存采集结果
        file_path = os.getcwd() + "/anjuke-result.xml"
        open(file_path,"wb").write(result)
        # 打印结果存放路径
        print("采集结果文件：" + file_path)
