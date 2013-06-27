import re
import string
import datetime

from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from inv_www.items import InvWwwItem
from scrapy.conf import settings
from scrapy import log
from scrapy.item import Item


class DrupalSpider(CrawlSpider):
    name = "penny.inv.www"
    allowed_domains = settings['PENNY_ALLOWEND_DOMAINS']
    start_urls = settings['DRUPAL_START_URLS']
    


    rules = (
        # Crawl filters
        Rule(SgmlLinkExtractor(allow=["terms", "dictionary"],allow_domains=allowed_domains), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        hxs = HtmlXPathSelector(response)
        i = InvWwwItem()
        properties = dict();

        if '?' in response.url:
            if 'page' not in response.url:
                i['path'] = response.url.split('?', 1)[0]
            else:
                i['path'] = response.url
        else:
            i['path'] = response.url

        i['timestamp'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        i['referer'] = response.request.headers.get('Referer')
        i['site'] = 'live'

        properties['title'] = hxs.select('/html/head/title/text()').extract()
        properties['robotsmeta'] = hxs.select('//meta[@id="Robots"]/@content').extract()
        properties['canonical'] = hxs.select('//link[@rel="canonical"]/@href').extract()
        properties['canonical'] = hxs.select('//link[@rel="canonical"]/@href').extract()
        properties['description'] = hxs.select('//meta[@name="description"]/@content').extract()
        properties['sailthrutitle'] = hxs.select('//meta[@id="MetaSailthruTitle"]/@name').extract()
        properties['sailthrudescription'] = hxs.select('//meta[@id="MetaSailthruDescription"]/@name').extract()
        properties['sailthrutags'] = hxs.select('//meta[@id="MetaSailthruTags"]/@name').extract()
        properties['sailthrudate'] = hxs.select('//meta[@id="MetaSailthruDate"]/@name').extract()
        properties['sailthruauthor'] = hxs.select('//meta[@id="MetaSailthruAuthor"]/@name').extract()
        properties['sailthruimagefull'] = hxs.select('//meta[@id="MetaSailthruImageFull"]/@name').extract()
        properties['sailthruimagethumb'] = hxs.select('//meta[@id="MetaSailthruImageThumb"]/@name').extract()
        properties['vibrant'] = hxs.select('//script[contains(@src, "intellitxt")]').extract()
        properties['pixel_targeting'] = hxs.select('//img[contains(@src, "fastclick")]/@src').extract()

        # Set defaults on the regex parsed values so they at least get a record in the database
        properties['googleanalytics'] = 'None'
        properties['comscore'] = 'None'
        properties['quantcast'] = 'None'
        properties['infolink'] = 'None'
        properties['oas_url'] = 'None'
        properties['oas_sitepage'] = 'None'
        properties['oas_listpos'] = 'None'
        properties['oas_query'] = 'None'
        properties['oa_source'] = 'None'
        properties['tms'] = 'None'
        properties['sailthruhorizon'] = 'None'
        properties['taxonomy'] = 'None'
        properties['adblade'] = 'None'
        properties['outbrain'] = 'None'
        properties['taboola'] = 'None'
        properties['dfp'] = 'None'

        scripts = hxs.select('//script')
        for script in scripts:
            content = script.extract()
            if '_gaq' in content:
                properties['googleanalytics'] = content

            if '_comscore' in content:
                properties['comscore'] = content

            if '_qevents' in content:
                properties['quantcast'] = content

            if 'infolink_pid' in content:
                infolink_script = hxs.select('//script[contains(@src, "infolinks")]').extract()
                properties['infolink'] = content + str(infolink_script)

            if 'OAS_url' in content:
                oas_url = re.search('OAS_url = \'([^;]*)\'', content, re.UNICODE)
                oas_sitepage = re.search('OAS_sitepage = \'([^;]*)\'', content, re.UNICODE)
                oas_listpos = re.search('OAS_listpos = \'([^;]*)\'', content, re.UNICODE)
                oas_query = re.search('OAS_query = \'([^;]*)\'', content, re.UNICODE)
                properties['oas_url'] = oas_url.group(1)
                properties['oas_sitepage'] = oas_sitepage.group(1)
                properties['oas_listpos'] = oas_listpos.group(1)
                properties['oas_query'] = oas_query.group(1)

            if 'OA_source' in content:
                oa_source = re.search('OA_source = \'([^;]*)\'', content, re.UNICODE)
                properties['oa_source'] = oa_source.group(1)

            if 'MasterTMS' in content:
                properties['tms'] = content

            if 'loadHorizon' in content:
                properties['sailthruhorizon'] = content

            if '_pageTaxonomy' in content:
                properties['taxonomy'] = content

            if 'outbrain.com' in content:
                properties['outbrain'] = content

            if 'adblade_' in content:
                properties['adblade'] = content

            if '_taboola' in content:
                properties['taboola'] = content

            if 'var googletag' in content:
                if properties['dfp'] is 'None':
                    properties['dfp'] = '';
                properties['dfp'] += content

            if 'googletag.enableServices' in content:
                if properties['dfp'] is 'None':
                    properties['dfp'] = '';
                properties['dfp'] += content


        i['properties'] = properties
        return i

SPIDER = DrupalSpider()
