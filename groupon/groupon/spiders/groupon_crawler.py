# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from groupon.items import GrouponItem


class GrouponCrawlerSpider(CrawlSpider):
    name = 'groupon_crawler'
    allowed_domains = ['groupon.com']
    start_urls = ['http://www.groupon.com/browse/los-angeles']

    rules = (
        Rule(LinkExtractor(allow=r'browse/los-angeles\?page=[0-17]'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        questions = (response).xpath('//figure[@class = "deal-card deal-list-tile deal-tile deal-tile-standard"]')

        for question in questions:
            item = GrouponItem()
            item['link'] = 'http:' + question.xpath('a/@href').extract()[0]
            item['title'] = question.xpath('a/figcaption/div/p[contains(@class,"deal-title")]/text()').extract()
            item['location'] = question.xpath('a/figcaption/div/p/span[@class="deal-location-name  "]/text()').extract()
            item['original_price'] = question.xpath(
                'a/figcaption/div/p/s[contains(@class,"original-price")]/text()').extract()
            item['price'] = question.xpath('a/figcaption/div/p/s[contains(@class,"discount-price")]/text()').extract()
            request = scrapy.Request(item['link'], callback=self.parse_likes)
            request.meta['item'] = item
            yield request

    def parse_likes(self, response):
        item = response.meta['item']
        like = (response).xpath('//div[@class = "deal-recs"]')
        likesratio = like.xpath('div/h3[@class = "classic-recommendations"]/meta/@content').extract()[0:2]
        item['likesratio'] = likesratio
        yield item
