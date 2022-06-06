from unicodedata import name
from pkg_resources import yield_lines
import scrapy
from yan_pa.items import YanPaItem

class VilpixSpider(scrapy.Spider):
    name = 'vilpix'
    # allowed_domains = ['www.vilipix.com']
    start_urls = ['http://www.vilipix.com/']

    page_num = 1

    def parse(self, response):
        nun = response.xpath('//*[@id="__layout"]/div/div[1]/section[1]/div/ul/li')
        for n in nun[:5]:
            item = YanPaItem()
            src = n.xpath('./div[1]/a/@href').extract_first()
            name = n.xpath('./div[2]/a/text()').extract_first()

            item['name'] = name

            detail_url = 'http://www.vilipix.com' + src
            yield scrapy.Request(detail_url,callback=self.pares_detail,meta={'item':item})


        #分页操作
        # if self.page_num <= 3:
        #     new_url = format(self.url%self.page_num)
        #     self.page_num += 1
        #     yield scrapy.Request(new_url,callback=self.parse)

        
    def pares_detail(self,response):
        item = response.meta['item']

        img_src = response.xpath('//*[@id="__layout"]/div/div[1]/div[2]/div/main/div/ul/li/a/img/@src').extract_first()
        img_src = img_src.split('?')[0]
        item['src'] = img_src
        yield item
