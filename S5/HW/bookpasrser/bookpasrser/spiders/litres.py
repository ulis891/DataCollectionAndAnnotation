import scrapy


class LitresSpider(scrapy.Spider):
    name = "litres"
    allowed_domains = ["litres.ru"]
    start_urls = ["https://www.litres.ru/search/?q=программирование"]

    def parse(self, response):
        next_page = response.xpath("//a[@data-qa='pager-next']/@href").get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)

        links = response.xpath('//a[@data-qa="serp-item__title"]/@href').getall()
        for link in links:
            yield response.follow(link, callback=self.vacancy_parse)
        pass
