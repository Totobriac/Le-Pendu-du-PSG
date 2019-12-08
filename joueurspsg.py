# -*- coding: utf-8 -*-
import scrapy

class BlogSpider(scrapy.Spider):
    name = 'characterspider'
    start_urls = ['https://fr.wikipedia.org/wiki/Liste_des_joueurs_du_Paris_Saint-Germain']

    def parse(self, response):
        for link in response.css('p:nth-child(1) a , p:nth-child(4) a, td:nth-child(1) a '):
            yield {'joueur': link.css('a ::text').extract()}

           
