import scrapy
from scrapy.http import HtmlResponse
from S5.HW.phoneparser.phoneparser.items import PhoneparserItem


class TacssafonSpider(scrapy.Spider):
    name = "tacssafon"
    allowed_domains = ["tacsafon.ru"]
    start_urls = ["https://tacsafon.ru/magazin/folder/mobilnyye-telefony"]
    phone_url = "https://tacsafon.ru"

    def parse(self, response):

        next_page = response.xpath("//li[@class='page-next']/a/@href").get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)

        links = response.xpath('//div[@class="product-name"]/a/@href').getall()
        for link in links:
            yield response.follow(self.phone_url + link, callback=self.vacancy_parse)

    def vacancy_parse(self, responce: HtmlResponse):
        name = responce.xpath("//h1/text()").get()
        price = responce.xpath("//div[@xpath='1']//text()").getall()
        url = responce.url
        info = responce.xpath("//ul[@class='shop2-color-ext-list']//div")
        region = info[0]
        color = info[1]
        yield PhoneparserItem(name=name, region=region, color=color, price=price, url=url)

    pass
