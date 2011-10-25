#coding: utf-8

""" 
    Scrape an HTML file to extract relevant     
  
    DEPENDENCIES:
        * lxml
        * datetime
        * re
"""

from lxml import html
    
def scrape(fd, conf):
    return scrapes(fd.read(), conf)
        
def scrapes(html_string, conf):
    page = html.fromstring(html_string)
    return process(page, conf)

def process(page, conf):
    result = {}
    for field in conf:
        xpath = conf[field]['xpath']
        scraped = page.xpath(xpath)
        
        if isinstance(scraped, list):
            scraped = map(lambda x : x.text, scraped)
        

        result[field] = scraped

        # scraped = scraped.strip()
        # scraped = re.sub("[\n\t]","",scraped)
        # if scraped in [None, '']:
        #     if 'default' in conf[field]:
        #         result[field] = conf[field]['default']
        # else:
        #     #encode field if character encoding is defined:
        #     if 'encoding' in conf[field]:
        #         encoding = conf[field]['encoding']
        #         if encoding is not None:
        #             try:
        #                 scraped = scraped.encode(encoding)
        #                 #utf-8 is the encoding needed by mysolr
        #                 scraped = unicode(scraped, "utf-8")
        #             except Exception as e:
        #                 logging.warn(e)
        #                 logging.warn("Error encoding %s field with provided encoding: %s" % (field, encoding))
        #                 logging.warn("  URL: %s" % url)
        #                 continue #dont include erroneous field
        #     #apply transformations (if defined)
        #     if 'transf' in conf[field]:
        #         value = scraped
        #         for func in conf[field]['transf']:
        #             try:
        #                 value = func(value)
        #             except Exception as e:
        #                 logging.error(e)
        #                 logging.error("Error applying %s transformation to %s field" % (func, field))
        #                 logging.error("  URL: %s" % url)
        #                 value = None
        #                 break #dont include erroneous field
        #         if value is not None: result[field] = value
        #         else: #we got None as a result of applying transformations
        #             if 'default' in conf[field]:
        #                 result[field] = conf[field]['default']
        #     else:
        #         result[field] = scraped
    return result	
    
