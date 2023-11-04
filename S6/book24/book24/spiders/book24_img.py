import scrapy
from scrapy.loader import ItemLoader
from scrapy.http import HtmlResponse

from S6.book24.book24.items import Book24Item


class Book24ImgSpider(scrapy.Spider):
    name = "book24_img"
    allowed_domains = ["book24.ru"]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.start_urls = [f"https://book24.ru/search/?q={kwargs.get('query')}"]

    # rules = (Rule(LinkExtractor(allow=r"Items/"), callback="parse_item", follow=True),)

    def parse(self, response: HtmlResponse):
        links = response.xpath("//div[@class='product-list__item']//a[@class='product-card__name']")
        for link in links:
            yield response.follow(link, callback=self.parse_book)

    def parse_book(self, response: scrapy.http.HtmlResponse):
        # name = response.xpath("//h1/text()").get()
        # price = response.xpath("//span[@class='app-price product-sidebar-price__price']/text()").get()
        # url = response.url
        # photos = response.xpath("//picture[@class='product-poster__main-picture']/source[1]/@srcset |"
        #                         "//picture[@class='product-poster__main-picture']/source[1]/@data-srcset").getall()
        # yield Book24Item(name=name, price=price, url=url, photos=photos)

        loader = ItemLoader(item=Book24Item(), response=response)
        loader.add_xpath('name', '//h1/text()')
        loader.add_xpath('price', "//span[@class='app-price product-sidebar-price__price']/text()")
        loader.add_value('url', response.url)
        loader.add_xpath('photos', "//picture[@class='product-poster__main-picture']/source[1]/@srcset |"
                                   "//picture[@class='product-poster__main-picture']/source[1]/@data-srcset")
        yield loader.load_item()
