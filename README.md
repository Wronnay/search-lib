# Wronnay Search Library
A library of classes which can be used to build a search engine.

Project inspired by the simple "Wronnay Search Engine" from 2014 (which is deprecated).

This project uses both, Python and PHP. (It's my first Python Project but my existing code from my search engine uses PHP).

When finished, this project will probably use Python (because it's the better solution for a search engine).

## General Information
License: GNU General Public License

Author: Christoph Daniel Miksche

Website: Actually none

## Dependencies

The crawler uses BeautifulSoup for handling the html code and MongoEngine for Data-Management.

BeautifulSoup will be shipped with this application. MongoEngine doesn't.

## Installation

Please install MongoEngine and MongoDB first:
```
pip install -U mongoengine
```
On Debian Servers:
```
apt install mongodb
```
Next steps: create a MongoDB Database and edit the lib/settings.py file.
