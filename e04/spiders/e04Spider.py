#e04Spider.py

import scrapy
from e04.items import E04Item
from scrapy_splash import SplashRequest
from scrapy.http import FormRequest
import logging
import re

class e04Spider(scrapy.Spider):
	name = "e04"
	start_url = 'https://www.104.com.tw/jobs/search/'
	def start_requests(self):
		queryStringList = [
			{
			'keyword':'python',
			'area':'6001001000',
			},
		]
		for queryString in queryStringList:
			yield FormRequest(url = self.start_url, method ='GET', \
				formdata = queryString, callback=self.detail_requests)
	def detail_requests(self, response):
		yield SplashRequest(response.request.url, self.deep_request, \
			meta = {'url':response.request.url},endpoint='render.html', \
			dont_filter = True)
	def depp_request(self, response):
		url = response.meta.get('url')
		html = response.text
		amount = int(re.findall('<meta.*-(.*?) 個工作機會.*',html)[0])
		page = int(amount / 20) + 1
		logging.info(page)
		for page in range(1,page+1)
			yield SplashRequest(url+"&page="+st(page), \
				endpoint='render.html', dont_filter=True)

			