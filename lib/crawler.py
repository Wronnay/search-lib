'''
Wronnay Search Library

Copyright 2016 Christoph Daniel Miksche
All rights reserved.

License: GNU General Public License
'''

import settings 	# Import the settings file
import urllib2		# Used to open URLs
import urlparse		# Parse URLs
import re
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
	Initialize the class and open a url
	'''
	def __init__(self, url):
		# Set url
		self.url = url
		# Open the url
		self.connection = self.openConnection(url)
		# html = result from connection
		self.html = self.connection
		# Create a BS instance
		self.soup = BeautifulSoup(self.html, "lxml")

	'''
	Open the connection to the website

	@author		Christoph Daniel Miksche (Wronnay)
	@date		31.10.2016
	@package 	WronnaySearchLib
	@since		Version 0.1
	@status 	UNTESTED!

	@param		String	url		The URL of the crawled entry.

	@return 					The Response (HTML-Code)
	'''
	def openConnection(self, url):

		opener = urllib2.build_opener()
		opener.addheaders = [('User-Agent', settings.useragent)]
		response = opener.open(url).read()

		return response

	'''
	Generate a ID of the crawled entry

	@author		Christoph Daniel Miksche (Wronnay)
	@date		23.10.2016
	@package 	WronnaySearchLib
	@since		Version 0.1
	@status 	UNTESTED!

	@return 	String			An sha1-Hash of the URL & SALT
	'''
	def generateID(self):
		# ToDo: Add some hashing algo here
		return url

	'''
	Get the Links of a Website

	@author		Christoph Daniel Miksche (Wronnay)
	@date		23.10.2016
	@package 	WronnaySearchLib
	@since		Version 0.1
	@status 	UNTESTED!

	@return 	List		links	A array with the crawled links of the site.
	'''
	def getLinks(self):

		# Create the links list
		linksList = []

		# Loop for the links
		for link in self.soup.find_all('a'):
			# Add link to list
			linksList.append(link.get('href'))

		# Return the links list
		return linksList


	'''
	Get the Title of a Website

	@author		Christoph Daniel Miksche (Wronnay)
	@date		31.10.2016
	@package 	WronnaySearchLib
	@since		Version 0.1
	@status 	UNTESTED!

	@return 	String		title	The Title of the Website
	'''
	def getTitle(self):
		return self.soup.title.string

	'''
	Get the meta tags of a Website

	@author		Christoph Daniel Miksche (Wronnay)
	@date		31.10.2016
	@package 	WronnaySearchLib
	@since		Version 0.1
	@status 	UNTESTED!

	@return 	List		Meta Tags of the Website
	'''
	def getMetaTags(self):
		out={}
		m = re.findall("name=\"([^\"]*)\" content=\"([^\"]*)\"", self.html)
		for i in m:
			out[i[0]] = i[1]
		return out


	'''
	Get the Description of a Website

	@author		Christoph Daniel Miksche (Wronnay)
	@date		31.10.2016
	@package 	WronnaySearchLib
	@since		Version 0.1
	@status 	UNTESTED!

	@return 	String		The Description of the Website
	'''
	def getDescription(self):

		metatags = self.getMetaTags()

		desc = metatags['description']

		return desc

	'''
	Get the Keywords of a Website

	@author		Christoph Daniel Miksche (Wronnay)
	@date		31.10.2016
	@package 	WronnaySearchLib
	@since		Version 0.1
	@status 	UNTESTED!

	@return 	String		The Keywords of the Website
	'''
	def getKeywords(self):

		metatags = self.getMetaTags()

		keyw = metatags['keywords']

		return keyw

	'''
	Get the Text of a Website

	@author		Christoph Daniel Miksche (Wronnay)
	@date		31.10.2016
	@package 	WronnaySearchLib
	@since		Version 0.1
	@status 	UNTESTED!

	@return 	String		text	The Text of the Website
	'''
	def getText(self):
		return self.soup.get_text()

	'''
	Get the Articles of a Website

	@author		Christoph Daniel Miksche (Wronnay)
	@date		31.10.2016
	@package 	WronnaySearchLib
	@since		Version 0.1
	@status 	UNTESTED!

	@return 	List		articles	A array with the crawled articles of the site.
	'''
	def getArticles(self):

		# Create the article list
		articleList = []

		# Loop for the articles
		for article in self.soup.find_all('article'):
			# Add article to list
			articleList.append(article.getText())

		# Return the article list
		return articleList

	'''
	Get the Paragraphs of a Website

	@author		Christoph Daniel Miksche (Wronnay)
	@date		31.10.2016
	@package 	WronnaySearchLib
	@since		Version 0.1
	@status 	UNTESTED!

	@return 	List		paragraphs 	A array with the crawled Paragraphs of the site.
	'''
	def getParagraphs(self):

		# Create the paragraph list
		paragraphList = []

		# Loop for the paragraphs
		for paragraph in self.soup.find_all('p'):
			# Add paragraph to list
			paragraphList.append(paragraph.getText())

		# Return the paragraph list
		return paragraphList


'''
CODE FOR TESTS

Test "getLinks"
 	crawl = Crawler('http://christoph.miksche.org')
	print(crawl.getLinks())

Test "getTitle"
	crawl = Crawler('http://christoph.miksche.org')
	print(crawl.getTitle())

Test "getText"
	crawl = Crawler('http://christoph.miksche.org')
	print(crawl.getText())

Test "getArticles"
	crawl = Crawler('http://blog.wronnay.net')
	print(crawl.getArticles())

Test "getParagraphs"
	crawl = Crawler('http://christoph.miksche.org')
	print(crawl.getParagraphs())

Test "getDescription"
	crawl = Crawler('http://board.wronnay.net/')
	print(crawl.getDescription())

Test "getKeywords"
	crawl = Crawler('http://board.wronnay.net/')
	print(crawl.getKeywords())

Test "getMetaTags"
	crawl = Crawler('http://board.wronnay.net/')
	print(crawl.getMetaTags())

'''
