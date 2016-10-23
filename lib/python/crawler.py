'''
Wronnay Search Library
 
Copyright 2016 Christoph Daniel Miksche
All rights reserved.

License: GNU General Public License
'''

import settings

'''
The Crawler Class
 
@author		Christoph Daniel Miksche (Wronnay)
@date		23.10.2016
@package 	WronnaySearchLib
@since		Version 0.1
'''
class Crawler:
	
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
	def generateID(url):
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
	def getLinks(url):
		
		# Create the links list
		links = []
		
		# ToDo: Add some crawling algo here
		
		# Return the links list
		return links	

