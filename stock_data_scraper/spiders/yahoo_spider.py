# https://doc.scrapy.org/en/latest/intro/tutorial.html
# https://stackoverflow.com/questions/46848323/how-to-get-the-max-historical-price-data-from-yahoo-finance

import scrapy

class YahooSpider(scrapy.Spider):
  name = 'yahoo'
  allowed_domains = ["finance.yahoo.com"]
  start_urls = ['https://finance.yahoo.com/quote/']
  STOCKS = {
    # name: shorthand
      'XIC': 'XIC.TO',
      'XEN': 'XEN.TO',
      'VUS': 'VUS.TO',
      'DSI': 'DSI',
      'VEF': 'VEF.TO',
      'ESGD': 'ESGD',
      'VEE': 'VEE.TO',
      'ESGE': 'ESGE',
      'VSB': 'VSB.TO',
      'CLF': 'CLF.TO',
      'ZEF': 'ZEF.TO',
      'VRE': 'VRE.TO',
      'REET': 'REET'
  }
  def start_requests(self):
    urls = []