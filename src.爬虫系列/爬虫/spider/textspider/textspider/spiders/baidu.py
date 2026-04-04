import scrapy


class BaiduSpider(scrapy.Spider):
    name = "baidu"
    allowed_domains = ["www.baidu.com"]
    start_urls = ["https://www.baidu.com"]

    def parse(self, response):
        #打印相应内容
        print(response.text)
        res=response.xpath('//*[@id="hotsearch-content-wrapper"]/li/a/span[2]')
        print("找到的内容：",res)
        for r in res:
            print(r.get())