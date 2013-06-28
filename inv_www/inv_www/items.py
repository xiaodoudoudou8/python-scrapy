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
        # touzi101 require crawl fields
        title = Field()
        keywords = Field()
        description = Field()

