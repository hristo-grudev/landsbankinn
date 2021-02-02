import scrapy

from scrapy.exceptions import CloseSpider
from scrapy.loader import ItemLoader
from ..items import LandsbankinnItem
from itemloaders.processors import TakeFirst


class LandsbankinnSpider(scrapy.Spider):
	name = 'landsbankinn'
	start_urls = ['https://www.landsbankinn.is/frettir']
	page = 1

	def parse(self, response):
		post_links = response.xpath('//div[@class="css-15b3szg-Center e1x0fnmm0"]/a/@href')
		yield from response.follow_all(post_links, self.parse_post)

		# self.page += 1
		# next_page = f'https://www.landsbankinn.is/frettir?page={self.page}'

		# if not post_links:
		# 	raise CloseSpider('no more pages')

		# yield response.follow(next_page, self.parse)

	def parse_post(self, response):
		title = response.xpath('//h1/text()').get()
		description = response.xpath('//div[@class="css-90lt5w-WrapText e1u9l8fo0"]/descendant-or-self::*/text()').getall()
		description = ' '.join(description)
		date = response.xpath('//div[@class="css-1pn9gs9-Date eomlx1u3"]/text()').get()

		item = ItemLoader(item=LandsbankinnItem(), response=response)
		item.default_output_processor = TakeFirst()
		item.add_value('title', title)
		item.add_value('description', description)
		item.add_value('date', date)

		return item.load_item()
