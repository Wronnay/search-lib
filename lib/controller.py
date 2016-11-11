'''
Wronnay Search Library

Copyright 2016 Christoph Daniel Miksche
All rights reserved.

License: GNU General Public License
'''

import Crawler 	    # Import the Crawler.
import Warehouse    # Import the Data Warehouse.

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
        crawl = new Crawler(url)
        siteTitle = crawl.getTitle()
        siteKeywords = crawl.getKeywords()
        siteDescription = crawl.getDescription()
        siteLinks = crawl.getLinks()
        # Save the Website
        save = new Warehouse()
        save.saveWebsite(url, siteTitle, siteDescription, siteKeywords, siteLinks)
