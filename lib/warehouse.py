'''
Wronnay Search Library

Copyright 2016 Christoph Daniel Miksche
All rights reserved.

License: GNU General Public License
'''
from mongoengine import *       # Import MongoEngine
import settings                 # Import the application settings.
import datetime
# Connect to MongoDB Database
connect(
    name=settings.connectionname,
    username=settings.dbusername,
    password=settings.dbpassword,
    host=settings.dbhost
)

'''
Define Website Document

@author		Christoph Daniel Miksche (Wronnay)
@date		11.11.2016
@package 	WronnaySearchLib
@since		Version 0.1
@status 	UNTESTED!
'''
class Website(Document):
    url = StringField(required=True)
    title = StringField(required=True)
    description = StringField()
    keywords = StringField()
    # text = StringField()
    date_modified = DateTimeField(default=datetime.datetime.now)
    links = ListField()


'''
The Warehouse Class

@author		Christoph Daniel Miksche (Wronnay)
@date		11.11.2016
@package 	WronnaySearchLib
@since		Version 0.1
'''
class Warehouse:

	'''
	Save the Data of a Website

	@author		Christoph Daniel Miksche (Wronnay)
	@date		11.11.2016
	@package 	WronnaySearchLib
	@since		Version 0.1
	@status 	UNTESTED!
	'''
    def saveWebsite(self, url, title, description, keywords, links):
        website = Website(url=url, title=title, description=description, keywords=keywords, links=links)
        website.save()
