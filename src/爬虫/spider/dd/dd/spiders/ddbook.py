import scrapy
import json

class DdbookSpider(scrapy.Spider):
    name = "ddbook"
    allowed_domains = ["e.dangdang.com"]
    start_urls = ["https://e.dangdang.com/media/api.go?action=mediaCategoryLeaf&promotionType=1&deviceSerialNo=html5&macAddr=html5&channelType=html5&permanentId=20251103151735850230850945041237376&returnType=json&channelId=70000&clientVersionNo=6.8.0&platformSource=DDDS-P&fromPlatform=106&deviceType=pconline&token=&start=0&end=20&category=ZTXYTL&dimension=dd_sale&order=0"]

    def parse(self, response):
        #解析数据
        res=json.loads(response.text)
        bookdata = res["data"]["saleList"]
        print("内容：",bookdata)
