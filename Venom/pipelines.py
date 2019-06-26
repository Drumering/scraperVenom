# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import re


class VenomPipeline(object):
    def process_item(self, item, spider):
        if item['R']:
            return item

class SaveDataPipeline(object):
    def open_spider(self,spider):
        self.arquivo = open("C:/Users/admin/eclipse-workspace/HasgardDeTouro-v0.1/src/br/com/opet/util/dadosWebCrawler.txt","a")
    def process_item(self, item, spider):
        print('aqui doidao',item['R'])
        colchao,preco = item['R']
        gerais = re.compile(r'^(.+?)[\s\(\-–#]+([\d,]+\s?x\s?[\d,]+\s?x\s?[\d,]+\s?(?:cm)?)')
        gerais = gerais.match(colchao)
        nome = gerais.group(1)
        tam = gerais.group(2)
        self.arquivo.write(nome + ' # ' + tam + ' # ' + preco + '\n')
        return item
    def close_spider(self,spider):
        self.arquivo.close()
