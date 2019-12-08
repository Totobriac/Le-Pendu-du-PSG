response.xpath(‘//a/@href’)

import scrapy

class BlogSpider(scrapy.Spider):
    name = 'characterspider'
    start_urls = ['https://fr.wikipedia.org/wiki/Liste_des_joueurs_du_Paris_Saint-Germain']

    def parse(self, response):
        for links in response.xpath('//td[(((count(preceding-sibling::*) + 1) = 1) and parent::*)]//a').getall():
            yield {"title": links}       

