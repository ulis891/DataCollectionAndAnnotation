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
        price = responce.xpath("//div[@class='price-product']//strong/text()").get()
        url = responce.url
        info = responce.xpath("//ul[@class='shop2-color-ext-list']//div//text()").getall()
        if len(info) > 4:
            region = info[1].strip()
            color = info[3].strip()
        else:
            region = None
            color = info[1].strip()
        full_info = responce.xpath("//table[@class='shop2-product-params']//td//text()").getall()
        rom = full_info[2].strip()
        ram = full_info[3]
        if "ГБ" not in ram:
            ram = None
        print(name, price, url, region, color, ram, rom)
        yield PhoneparserItem(name=name, region=region, color=color, price=price, ram=ram, rom=rom, url=url)

