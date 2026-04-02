import scrapy


class ZpdataSpider(scrapy.Spider):
    name = "zpdata"
    allowed_domains = ["zhaopin.com"]
    start_urls = ["https://www.zhaopin.com/sou/jl749/kw01O00U80EG06G03F01N0/p1"]

    def parse(self, response):
        #拿到相应数据response

        datas = response.xpath('//*[@id="positionList-hook"]/div/div[1]/div')
        print("20条数据",datas)
        for data in datas:
            #岗位信息
            job_info = data.xpath('.//div[@class="jobinfo__name"]/text()')
            print("岗位信息",job_info)
            #岗位

