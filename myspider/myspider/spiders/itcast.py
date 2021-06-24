import scrapy
from myspider.items import MyspiderItem


class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['itcast.cn']
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml#ajavaee']

    def parse(self, response):
         # scrapy的response对象可以直接进行xpath
        names = response.xpath('//div[@class="tea_con"]//li/div/h3/text()') 
        print(names)

        # 获取具体数据文本的方式如下
        # 分组
        li_list = response.xpath('//div[@class="tea_con"]//li') 
        for li in li_list:
            # 创建一个数据字典
            #item = {}
            item = MyspiderItem()
            # 利用scrapy封装好的xpath选择器定位元素，并通过extract()或extract_first()来获取结果
            item['name'] = li.xpath('.//h3/text()').extract_first() # 老师的名字
            item['level'] = li.xpath('.//h4/text()').extract_first() # 老师的级别
            item['text'] = li.xpath('.//p/text()').extract_first() # 老师的介绍
            yield item
