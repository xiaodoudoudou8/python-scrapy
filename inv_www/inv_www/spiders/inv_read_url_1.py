import re
import string
import datetime
import MySQLdb


from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
#from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.spider import BaseSpider
from inv_www.items import InvWwwItem
from scrapy.conf import settings
from scrapy import log
from scrapy.item import Item
from os import path
from scrapy import signals
from scrapy.xlib.pydispatch import dispatcher 


class InvcnSpider(BaseSpider):
    name = "inv-cn"
    allowed_domains = settings['ALLOWEND_DOMAINS']
    filename = 'crawledlist.txt'
    
    def __init__(self):
        start_urls = []
        self.header = settings['HEADER']
        urlfilename = '../../urlfile/invcn-url.txt'#/inv/crawl/code/urlfile/
        urlfile = open(urlfilename)
 
        while 1:
            lines = [l.strip() for l in urlfile.readlines(100000)]
            if not lines:
                break
            for line in lines:
                start_urls.append(self.header+line)
        self.start_urls = start_urls  
	#=============================end

#   def parse_item(self, response):
    def parse(self, response):
        start_urls = self.start_urls
        hxs = HtmlXPathSelector(response)
        i = InvWwwItem()
        keys = dict()
        keys['path'] = 'None'
        keys['keywords'] = 'None'
        keys['description'] = 'None'
        keys['title'] = 'None'
        keys['timestamp'] = 'None'
        i['path'] = response.url.replace(self.header,"")  
        i['timestamp'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        i['title'] = hxs.select('/html/head/title/text()').extract()
        i['description'] = hxs.select('//meta[@name="description"]/@content').extract()
        i['keywords'] = hxs.select('//meta[@name="Keywords"]/@content').extract()
        print "path:%s title:%s description:%s keywords:%s" % (i['path'], i['title'], i['description'], i['keywords'])
        self.f.write("path:" + i['path'] + " " + "title:" + i['title'] + " " + "description:" + i['description'] + " " + "keywords:" + i['keywords'])
        return i
    def open(self):
        if path.exists(self.filename):            
            self.f = open(self.filename, 'a')        
        else:
            self.f = open(self.filename, 'w')     
    def close(self):        
        self.f.close() if self.f is not None else None

SPIDER = InvcnSpider()

