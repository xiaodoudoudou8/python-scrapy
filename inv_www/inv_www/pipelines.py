# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html


from scrapy.conf import settings
import MySQLdb
import sys
from scrapy import log

def connect():
    conn = MySQLdb.connect(host=settings['SAVEHOST'], user=settings['SAVEUSER'], passwd=settings['SAVEPASSWORD'], db=settings['SAVEDB'], charset = "utf8", use_unicode = True)
    return conn
db = connect()

class InvWwwPipeline(object):
    def process_item(self, item, spider):
        global db
    cursor = db.cursor()
      #   try:   
      #           for k in item['keys'].keys():
      #               if type(item[k]) == list:
		    #    if (len(item[k])) > 0:
      #                      item[k] = item[k][0]
                   
		    #    #print "========================> %s with length %s" % (k, item[k])
		    
      #               if len(item[k]) >0:
      #                  #pass
      #                 item[k] = item[k].strip()
      #               else:
      #                  item[k] = 'None'
      #           if item['site'] == 'staging':                
		    # cursor.execute("""INSERT INTO crawler_page_staging (time, crawlernum, weight, path, timestamp, referer, site, adblade, canonical, comscore, description, dfp, googleanalytics, infolink, oas_listpos, oas_query, oas_sitepage, oas_url, oa_source, outbrain, pixel_targeting, quantcast, robotsmeta, sailthrudate, sailthruauthor, sailthrudescription, sailthruhorizon, sailthruimagethumb, sailthrutags, sailthruimagefull, sailthrutitle, taboola, taxonomy, title, tms, vibrant) VALUES (now(), %s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""", \
      #                  (item['crawlernum'], item['weight'], item['path'], item['timestamp'], item['referer'], item['site'], item['adblade'], item['canonical'], item['comscore'], item['description'], item['dfp'], item['googleanalytics'], item['infolink'], item['oas_listpos'], item['oas_query'], item['oas_sitepage'], item['oas_url'], item['oa_source'], item['outbrain'], item['pixel_targeting'], item['quantcast'], item['robotsmeta'], item['sailthrudate'], item['sailthruauthor'], item['sailthrudescription'], item['sailthruhorizon'], item['sailthruimagethumb'], item['sailthrutags'], item['sailthruimagefull'], item['sailthrutitle'], item['taboola'], item['taxonomy'], item['title'], item['tms'], item['vibrant']))
      #           elif item['site'] =='live':
		    # cursor.execute("""INSERT INTO crawler_page_staging (time, crawlernum, weight, path, timestamp, referer, site, adblade, canonical, comscore, description, dfp, googleanalytics, infolink, oas_listpos, oas_query, oas_sitepage, oas_url, oa_source, outbrain, pixel_targeting, quantcast, robotsmeta, sailthrudate, sailthruauthor, sailthrudescription, sailthruhorizon, sailthruimagethumb, sailthrutags, sailthruimagefull, sailthrutitle, taboola, taxonomy, title, tms, vibrant) VALUES (now(), %s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""", \
      #                  (item['crawlernum'], item['weight'], item['path'], item['timestamp'], item['referer'], item['site'], item['adblade'], item['canonical'], item['comscore'], item['description'], item['dfp'], item['googleanalytics'], item['infolink'], item['oas_listpos'], item['oas_query'], item['oas_sitepage'], item['oas_url'], item['oa_source'], item['outbrain'], item['pixel_targeting'], item['quantcast'], item['robotsmeta'], item['sailthrudate'], item['sailthruauthor'], item['sailthrudescription'], item['sailthruhorizon'], item['sailthruimagethumb'], item['sailthrutags'], item['sailthruimagefull'], item['sailthrutitle'], item['taboola'], item['taxonomy'], item['title'], item['tms'], item['vibrant']))
      #           else:
		    # cursor.execute("""INSERT INTO crawler_page_drupal (time, crawlernum, weight, path, timestamp, referer, site, adblade, canonical, comscore, description, dfp, googleanalytics, infolink, oas_listpos, oas_query, oas_sitepage, oas_url, oa_source, outbrain, pixel_targeting, quantcast, robotsmeta, sailthrudate, sailthruauthor, sailthrudescription, sailthruhorizon, sailthruimagethumb, sailthrutags, sailthruimagefull, sailthrutitle, taboola, taxonomy, title, tms, vibrant) VALUES (now(), %s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""", \
      #                  (item['crawlernum'], item['weight'], item['path'], item['timestamp'], item['referer'], item['site'], item['adblade'], item['canonical'], item['comscore'], item['description'], item['dfp'], item['googleanalytics'], item['infolink'], item['oas_listpos'], item['oas_query'], item['oas_sitepage'], item['oas_url'], item['oa_source'], item['outbrain'], item['pixel_targeting'], item['quantcast'], item['robotsmeta'], item['sailthrudate'], item['sailthruauthor'], item['sailthrudescription'], item['sailthruhorizon'], item['sailthruimagethumb'], item['sailthrutags'], item['sailthruimagefull'], item['sailthrutitle'], item['taboola'], item['taxonomy'], item['title'], item['tms'], item['vibrant']))

      #           db.commit()
      #   except Exception as e:
      #           print cursor
      #           print e
                #db.rollback()

	#db.close()

        return item
       