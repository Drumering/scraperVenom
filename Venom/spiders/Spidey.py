# -*- coding: utf-8 -*-
import scrapy


class SpideySpider(scrapy.Spider):
    name = 'Spidey'
    allowed_domains = ['https://www.casatema.com.br/moveis/infantis/colchao-infantil']
    start_urls = ['https://www.casatema.com.br/moveis/infantis/colchao-infantil']

    def parse(self, response):
        colchoes = response.xpath("//div[@class='shelf-qd-v1-name']//a/@title").extract()
        precos = response.xpath("//a//span/@data-price").extract()
        itens = zip(colchoes,precos)
        print('precos',precos)
        for item in list(itens):
            print(item)
            yield {'R':item}
