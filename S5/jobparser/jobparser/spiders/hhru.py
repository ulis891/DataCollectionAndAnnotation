import scrapy
from scrapy.http import HtmlResponse
from S5.jobparser.jobparser.items import JobparserItem


class HhruSpider(scrapy.Spider):
    name = "hhru"
    allowed_domains = ["hh.ru"]
    start_urls = ["https://hh.ru/search/vacancy?text=Python&from=suggest_post&area=1&hhtmFrom=main"]

    def parse(self, response: HtmlResponse):

        next_page = response.xpath("//a[@data-qa='pager-next']/@href").get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)

        links = response.xpath('//a[@data-qa="serp-item__title"]/@href').getall()
        for link in links:
            yield response.follow(link, callback=self.vacancy_parse)


    def vacancy_parse(self, responce:HtmlResponse):
        name = responce.xpath("//h1/text()").get()
        salary = responce.xpath("//div[@data-qa='vacancy-salary']//text()").getall()
        url = responce.url
        yield JobparserItem(name=name, salary=salary, url=url)