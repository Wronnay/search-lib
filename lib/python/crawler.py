'''
Wronnay Search Library
 
Copyright 2016 Christoph Daniel Miksche
All rights reserved.

License: GNU General Public License
'''

import settings 	# Import the settings file
import urllib2		# Used to open URLs
import urlparse		# Parse URLs
from bs4 import BeautifulSoup	# Import BeautifulSoap to handle the html

'''
The Crawler Class
 
@author		Christoph Daniel Miksche (Wronnay)
@date		23.10.2016
@package 	WronnaySearchLib
@since		Version 0.1
'''
class Crawler:
	
	'''
	Initialize the class and gave it a name
	'''
	def __init__(self, name):
		self.name = name
	
	'''
	Generate a ID of the crawled entry
	 
	@author		Christoph Daniel Miksche (Wronnay)
	@date		23.10.2016
	@package 	WronnaySearchLib
	@since		Version 0.1
	@status 	UNTESTED!
	 
	@param		String	url		The URL of the crawled entry.
	 
	@return 	String			An sha1-Hash of the URL & SALT
	'''
	def generateID(self, url):
		# ToDo: Add some hashing algo here
		return url

	'''
	Get the Links of a Website
	 
	@author		Christoph Daniel Miksche (Wronnay)
	@date		23.10.2016
	@package 	WronnaySearchLib
	@since		Version 0.1
	@status 	UNTESTED!
	
	@param		String		url		The URL which should be crawled.
	
	@return 	List		links	A array with the crawled links of the site.
	'''	
	def getLinks(self, url):
		
		# Create the links list
		linksList = []
		
		# Open the url
		html = urllib2.urlopen(url).read()
		
		# Create a BS instance
		soup = BeautifulSoup(html, "lxml")
		
		# Loop for the links
		for link in soup.find_all('a'):
			# Add link to list
			linksList.append(link.get('href'))
		
		# ToDo: Add some crawling algo here
		
		# Return the links list
		return linksList	

# Test the crawler

crawl = Crawler('crawl')
print(crawl.getLinks('http://christoph.miksche.org'))
