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
#penny dev test
#PENNY_ALLOWEND_DOMAINS = ["www.staging.investopedia.com"]
#PENNY_ALLOWEND_DOMAINS = ["www.investopedia.com"]
#PENNY_ALLOWEND_DOMAINS = ["dev2.investopedia.com"]
PENNY_ALLOWEND_DOMAINS = ["staging.vcinv.net"]
#drupal staging domain http://staging.admin.vcinv.net/

#HEADER = "http://www.staging.investopedia.com"
#HEADER = "http://dev2.investopedia.com"
#HEADER = "http://www.investopedia.com"
HEADER = "http://staging.vcinv.net/"

#PENNYHOST = "cmsfdb101.beta.wl.mezimedia.com"
PENNYHOSTREADURL = "10.32.28.10"
PENNYHOST= "10.32.28.11"#"db102.dev.wl.vcinv.net"
#PENNYHOST = "db101.dev.wl.vcinv.net"
PENNYUSER = "dt_cms"
PENNYPASSWORD = "dtCms23!"
PENNYDB = "INV_Staging"
PENNYDBREADURL = "crawler"
#end penny dev test

#DRUPAL_START_URLS      =   ["http://www.staging.investopedia.com/"]

#self.header = "http://www.staging.investopedia.com"
#self.header = "http://dev2.investopedia.com"
#self.header = "http://www.investopedia.com"