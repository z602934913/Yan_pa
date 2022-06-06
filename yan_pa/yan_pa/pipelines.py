# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.pipelines.images import ImagesPipeline
import scrapy

class YanPaPipeline:
    def process_item(self, item, spider):
        return item

class imgsPileLine(ImagesPipeline):

    #根据图片地址获取图片数据(二进制)
    def get_media_requests(self, item, info):
        yield scrapy.Request(item['src'])

    #存储路径
    def file_path(self, request, response=None, info=None, *, item=None):
        # return super().file_path(request, response, info, item=item)
        imgNameType = request.url.split('.')[-1]
        imgName = item['name'] + '.' +imgNameType
        print('-----Download:%s----complete' % (item['name']))
        return imgName

    def item_completed(self, results, item, info):
        # return super().item_completed(results, item, info)
        return item