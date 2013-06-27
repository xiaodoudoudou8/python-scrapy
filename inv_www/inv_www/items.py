# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class InvWwwItem(Item):
    # define the fields for your item here like:
    # name = Field()
        path = Field()
        timestamp = Field()
        referer = Field()
        site = Field()
        adblade = Field()
        canonical = Field()
        comscore = Field()
        description = Field()
        dfp = Field()
        googleanalytics = Field()
        infolink = Field()
        oas_listpos = Field()
        oas_query = Field()
        oas_sitepage = Field()
        oas_url = Field()
        oa_source = Field()
        outbrain = Field()
        pixel_targeting = Field()
        quantcast = Field()
        robotsmeta = Field()
        sailthrudate = Field()
        sailthruauthor = Field()
        sailthrudescription = Field()
        sailthruhorizon = Field()
        sailthruimagethumb = Field()
        sailthrutags = Field()
        sailthruimagefull = Field()
        sailthrutitle = Field()
        taboola = Field()
        taxonomy = Field()
        title = Field()
        tms = Field()
        vibrant = Field()
	keys = Field()
        weight = Field()
	crawlernum = Field()