# # https://doc.scrapy.org/en/latest/intro/tutorial.html
# # https://stackoverflow.com/questions/46848323/how-to-get-the-max-historical-price-data-from-yahoo-finance

# import scrapy

# class YahooSpider(scrapy.Spider):
#   name = 'yahoo'
#   allowed_domains = ["finance.yahoo.com"]
#   start_urls = ['https://finance.yahoo.com/quote/']
#   STOCKS = {
#     # name: shorthand
#       'XIC': 'XIC.TO',
#       'XEN': 'XEN.TO',
#       'VUS': 'VUS.TO',
#       'DSI': 'DSI',
#       'VEF': 'VEF.TO',
#       'ESGD': 'ESGD',
#       'VEE': 'VEE.TO',
#       'ESGE': 'ESGE',
#       'VSB': 'VSB.TO',
#       'CLF': 'CLF.TO',
#       'ZEF': 'ZEF.TO',
#       'VRE': 'VRE.TO',
#       'REET': 'REET'
#   }
#   def start_requests(self):
#     urls = []

import scrapy
import time


class FinanceSpider(scrapy.Spider):
    name = "finance"
    allowed_domains = ["finance.yahoo.com"]
    start_urls = ['https://finance.yahoo.com/quote/FB']

    def parse(self, response):
        crumb = response.css('script').re_first('user":{"crumb":"(.*?)"').decode('unicode_escape')
        url = ("https://query1.finance.yahoo.com/v7/finance/download/FB" +
               "?period1=-2208988800&period2=" + str(int(time.time())) + "&interval=1d&events=history&" +
               "crumb={}".format(crumb))
        return scrapy.Request(url, callback=self.parse_csv)

    def parse_csv(self, response):
        lines = response.body.strip().split('\n')
        print(lines[0])
        print(lines[1])
        print(lines[-1])