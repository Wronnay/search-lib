'''
Wronnay Search Library

Copyright 2016 Christoph Daniel Miksche
All rights reserved.

License: GNU General Public License
'''
import time
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
    Index a Website (without Metainformation).

    @author		Christoph Daniel Miksche (Wronnay)
    @date		11.11.2016
    @package 	WronnaySearchLib
    @since		Version 0.1
    @status 	UNTESTED!
    '''

    def indexWebsite(self, url):
        try:
            # Crawl the Website
            crawl = Crawler(url)
            siteLinks = crawl.getLinks()
            # Save the Website
            save = Warehouse()
            save.saveWebsite(url, siteLinks)
            # Return the next Links to crawl.
            return siteLinks
        except:
            pass    # ignore errors!

    '''
    Index a Website with Metatags

    @author		Christoph Daniel Miksche (Wronnay)
    @date		12.11.2016
    @package 	WronnaySearchLib
    @since		Version 0.1
    @status 	UNTESTED!
    '''

    def indexMetaWebsite(self, url):
        try:
            # Crawl the Website
            crawl = Crawler(url)
            siteTitle = crawl.getTitle()
            # Crawl more Metatags:
            siteKeywords = crawl.getKeywords()
            siteDescription = crawl.getDescription()
            siteLinks = crawl.getLinks()
            # Save the Website
            save = Warehouse()
            # Save more Metatags:
            save.saveMetaWebsite(url, siteTitle, siteDescription, siteKeywords, siteLinks)
            # Return the next Links to crawl.
            return siteLinks
        except:
            pass    # ignore errors!

    '''
    Index a Website and the linked Websites (with end).

    @author		Christoph Daniel Miksche (Wronnay)
    @date		12.11.2016
    @package 	WronnaySearchLib
    @since		Version 0.1
    @status 	UNTESTED!
    '''
    def indexLinks(self, url):
        links = self.indexWebsite(url)
        urlArray = []

        for link in links:
            urlArray.append(self.indexWebsite(link))

        return urlArray

    '''
    Index a Website and the linked Websites without end.

    @author		Christoph Daniel Miksche (Wronnay)
    @date		12.11.2016
    @package 	WronnaySearchLib
    @since		Version 0.1
    @status 	UNTESTED!
    '''
    def indexInfinityLinks(self, url):
        links = self.indexWebsite(url) # array for links.

        for link in links:
            links.append(self.indexWebsite(link)) # get links from website and add to array.

    '''
    Index a Website and the linked Websites without end.

    @author		Christoph Daniel Miksche (Wronnay)
    @date		12.11.2016
    @package 	WronnaySearchLib
    @since		Version 0.1
    @status 	UNTESTED!
    '''
    def indexInfinityLinksAndSleep(self, url):
        links = self.indexWebsite(url) # array for links.

        for link in links:
            links.append(self.indexWebsite(link)) # get links from website and add to array.
            links.remove(link) # remove the actual link (to save space).
            time.sleep(1) # sleep one second after every website (for a better cpu livetime).

'''
CODE FOR TESTS

Test "indexWebsite"
    cont = Controller()
    print(cont.indexWebsite('http://board.wronnay.net'))
Test "indexLinks"
    cont = Controller()
    print(cont.indexLinks('http://christoph.miksche.org'))
Test "indexInfinityLinks" (WARNING: PROCESS WILL NOT END!)
    cont = Controller()
    print(cont.indexInfinityLinks('http://christoph.miksche.org'))
'''
cont = Controller()
print(cont.indexInfinityLinksAndSleep('http://christoph.miksche.org'))
