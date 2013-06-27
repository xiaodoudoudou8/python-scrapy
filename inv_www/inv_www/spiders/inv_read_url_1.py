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


class InvStagingReadUrl1Spider(BaseSpider):
    name = "inv.staging.read.url.1"
    allowed_domains = settings['PENNY_ALLOWEND_DOMAINS']
    #allowed_domains = "www.investopedia.com"
    #allowed_domains = "www.staging.investopedia.com"
    #allowed_domains = "dev2.investopedia.com"
    filename = 'uncrawledlist.txt'
    
    def __init__(self):
        start_urls = []
        #self.header = "http://www.staging.investopedia.com"
	#self.header = "http://dev2.investopedia.com"
	#self.header = "http://www.investopedia.com"
	self.header = settings['HEADER']
        conn = MySQLdb.connect(host=settings['PENNYHOST'], user=settings['PENNYUSER'], passwd=settings['PENNYPASSWORD'], db=settings['PENNYDB'], port=3306)
        cur = conn.cursor()
	#cur.execute("SELECT Path FROM crawlerUrl limit 0,6970")
        cur.execute("select alias as path from INV_Staging.devel_url_alias limit 0,6970")
        rows = cur.fetchall()
        for row in rows:
            #print self.header+row[0]
            start_urls.append(self.header+row[0])   
        self.start_urls = start_urls 
       
        conn. close()
	
	self.f = None        
        dispatcher.connect(self.open, signals.engine_started)        
        dispatcher.connect(self.close, signals.engine_stopped)  
	#=============================end

#   def parse_item(self, response):
    def parse(self, response):
	start_urls = self.start_urls
        hxs = HtmlXPathSelector(response)
	if response.status != 200:
            self.f.write(str(response.status)+" : "+str(response.url)+ '\n')
        i = InvWwwItem()
        keys = dict()
        keys['adblade']= 'None'
	keys['canonical'] = 'None'
	keys['comscore'] = 'None'
	keys['description'] = 'None'
	keys['dfp'] = 'None'
	keys['googleanalytics'] = 'None'
	keys['infolink'] = 'None'
	keys['oas_listpos'] = 'None'
	keys['oas_query'] = 'None'
	keys['oas_sitepage'] = 'None'
	keys['oas_url'] = 'None'
	keys['oa_source'] = 'None'
	keys['outbrain'] = 'None'
	keys['pixel_targeting'] = 'None'
	keys['quantcast'] = 'None'
	keys['robotsmeta'] = 'None'
	keys['sailthrudate'] = 'None'
	keys['sailthruauthor'] = 'None'
	keys['sailthrudescription'] = 'None'
	keys['sailthruhorizon'] = 'None'
	keys['sailthruimagethumb'] = 'None'
	keys['sailthrutags'] = 'None'
	keys['sailthruimagefull'] = 'None'
	keys['sailthrutitle'] = 'None'
	keys['taboola'] = 'None'
	keys['taxonomy'] = 'None'
	keys['title'] = 'None'
	keys['tms'] = 'None'
	keys['vibrant'] = 'None'    
        i['keys'] = keys
	i['crawlernum'] = '1'
        if '?' in response.url:
            if 'page' not in response.url:
                i['path'] = response.url.split('?', 1)[0].replace(self.header,"")
            else:
                i['path'] = response.url.replace(self.header,"")
        else:
            i['path'] = response.url.replace(self.header,"")  
        i['timestamp'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        i['referer'] = response.request.headers.get('Referer')

	if not i['referer']:
	    i['referer'] = 'None'

        i['title'] = hxs.select('/html/head/title/text()').extract()
        i['robotsmeta'] = hxs.select('//meta[@id="Robots"]/@content').extract()
        i['canonical'] = hxs.select('//link[@rel="canonical"]/@href').extract()
        i['description'] = hxs.select('//meta[@name="description"]/@content').extract()
        i['sailthrutitle'] = hxs.select('//meta[@id="MetaSailthruTitle"]/@name').extract()
        i['sailthrudescription'] = hxs.select('//meta[@id="MetaSailthruDescription"]/@name').extract()
        i['sailthrutags'] = hxs.select('//meta[@id="MetaSailthruTags"]/@name').extract()
        i['sailthrudate'] = hxs.select('//meta[@id="MetaSailthruDate"]/@name').extract()
        i['sailthruauthor'] = hxs.select('//meta[@id="MetaSailthruAuthor"]/@name').extract()
        i['sailthruimagefull'] = hxs.select('//meta[@id="MetaSailthruImageFull"]/@name').extract()
        i['sailthruimagethumb'] = hxs.select('//meta[@id="MetaSailthruImageThumb"]/@name').extract()
        i['vibrant'] = hxs.select('//script[contains(@src, "intellitxt")]').extract()
        i['pixel_targeting'] = hxs.select('//img[contains(@src, "fastclick")]/@src').extract()

        # Set defaults on the regex parsed values so they at least get a record in the database
        i['googleanalytics'] = 'None'
        i['comscore'] = 'None'
        i['quantcast'] = 'None'
        i['infolink'] = 'None'
        i['oas_url'] = 'None'
        i['oas_sitepage'] = 'None'
        i['oas_listpos'] = 'None'
        i['oas_query'] = 'None'
        i['oa_source'] = 'None'
        i['tms'] = 'None'
        i['sailthruhorizon'] = 'None'
        i['taxonomy'] = 'None'
        i['adblade'] = 'None'
        i['outbrain'] = 'None'
        i['taboola'] = 'None'
        i['dfp'] = 'None'


	scripts = hxs.select('//script')
        for script in scripts:
            content = script.extract()

            if '_gaq' in content:
                i['googleanalytics'] = content

            if '_comscore' in content:
                i['comscore'] = content

            if '_qevents' in content:
                i['quantcast'] = content

            if 'infolink_pid' in content:
                infolink_script = hxs.select('//script[contains(@src, "infolinks")]').extract()
                i['infolink'] = content + str(infolink_script)

            if 'OAS_url' in content:
                oas_url = re.search('OAS_url = \'([^;]*)\'', content, re.UNICODE)
                oas_sitepage = re.search('OAS_sitepage = \'([^;]*)\'', content, re.UNICODE)
                oas_listpos = re.search('OAS_listpos = \'([^;]*)\'', content, re.UNICODE)
                oas_query = re.search('OAS_query = \'([^;]*)\'', content, re.UNICODE)
                i['oas_url'] = oas_url.group(1)
                i['oas_sitepage'] = oas_sitepage.group(1)
                i['oas_listpos'] = oas_listpos.group(1)
                i['oas_query'] = oas_query.group(1)

            if 'OA_source' in content:
                oa_source = re.search('OA_source = \'([^;]*)\'', content, re.UNICODE)
                i['oa_source'] = oa_source.group(1)

            if 'MasterTMS' in content:
                i['tms'] = content

            if 'loadHorizon' in content:
                i['sailthruhorizon'] = content

            if '_pageTaxonomy' in content:
                i['taxonomy'] = content

            if 'outbrain.com' in content:
                i['outbrain'] = content

            if 'adblade_' in content:
                i['adblade'] = content

            if '_taboola' in content:
                i['taboola'] = content

            if 'var googletag' in content:
                if i['dfp'] is 'None':
                    i['dfp'] = '';
                i['dfp'] += content

            if 'googletag.enableServices' in content:
                if i['dfp'] is 'None':
                    i['dfp'] = '';
                i['dfp'] += content
           
        return i
    def open(self):
        if path.exists(self.filename):            
            self.f = open(self.filename, 'a')        
        else:
            self.f = open(self.filename, 'w')     
    def close(self):        
        self.f.close() if self.f is not None else None

SPIDER = InvStagingReadUrl1Spider()
