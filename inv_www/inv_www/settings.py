# Scrapy settings for inv_www project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#
import os
import re

BOT_NAME = 'inv_www'
BOT_VERSION = '1.0'
LOG_ENABLED = False
DOWNLOAD_TIMEOUT = 120      # 3mins
SPIDER_MODULES = ['inv_www.spiders']
NEWSPIDER_MODULE = 'inv_www.spiders'
DEFAULT_ITEM_CLASS = 'inv_www.items.InvWwwItem'
ITEM_PIPELINES = ['inv_www.pipelines.InvWwwPipeline']

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'inv_www (+http://www.yourdomain.com)'
#PENNY_ALLOWEND_DOMAINS = ["touzi101dev1.vcbrands.com"]
ALLOWEND_DOMAINS = ["www.touzi101.cn"]
#drupal staging domain 
#HEADER = "http://touzi101dev1.vcbrands.com"
HEADER = "http://www.touzi101.cn/"


SAVEHOST= "10.32.28.11"

SAVEUSER = ""
SAVEPASSWORD = ""
SAVEDB = ""
#end penny dev test
