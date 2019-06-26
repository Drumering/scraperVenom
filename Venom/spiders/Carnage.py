# -*- coding: utf-8 -*-
import scrapy


class CarnageSpider(scrapy.Spider):
    name = 'Carnage'
    allowed_domains = ['https://www.costaricacolchoes.com.br/loja/colchao/']
    start_urls = ['https://www.costaricacolchoes.com.br/loja/colchao/']

    def parse(self, response):
        colchoes = response.xpath("//div[@class='departamento-gira full']//span[@class='nome-destaque']//text()").extract()
        precos = response.xpath("//div[@class='departamento-gira full']//span[@class='preco-avista']/text()").extract()
        itens = zip(colchoes,precos)
        for item in list(itens):
            yield {'R':item}
