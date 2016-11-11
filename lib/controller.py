'''
Wronnay Search Library

Copyright 2016 Christoph Daniel Miksche
All rights reserved.

License: GNU General Public License
'''
from crawler import * 	    # Import the Crawler.
from warehouse import *   # Import the Data Warehouse.

'''
The Controller Class

@author		Christoph Daniel Miksche (Wronnay)
@date		11.11.2016
@package 	WronnaySearchLib
@since		Version 0.1
'''


class Controller:

    '''
    Index a Website

    @author		Christoph Daniel Miksche (Wronnay)
    @date		11.11.2016
    @package 	WronnaySearchLib
    @since		Version 0.1
    @status 	UNTESTED!
    '''

    def indexWebsite(self, url):
        # Crawl the Website
        crawl = Crawler(url)
        siteTitle = crawl.getTitle()
        siteKeywords = crawl.getKeywords()
        siteDescription = crawl.getDescription()
        siteLinks = crawl.getLinks()
        # Save the Website
        save = Warehouse()
        save.saveWebsite(url, siteTitle, siteDescription, siteKeywords, siteLinks)
        # Return the next Links to crawl.
        return siteLinks

'''
CODE FOR TESTS

Test "indexWebsite"
    cont = Controller()
    print(cont.indexWebsite('http://board.wronnay.net'))
'''
cont = Controller()
print(cont.indexWebsite('http://board.wronnay.net'))
