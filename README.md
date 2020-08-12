# Wronnay Search Library

[![PyPI version](https://badge.fury.io/py/wronnay-search-lib.svg)](https://badge.fury.io/py/wronnay-search-lib)
[![Downloads](https://pepy.tech/badge/wronnay-search-lib)](https://pepy.tech/project/wronnay-search-lib)

A library of classes which can be used to build a search engine.

Project inspired by the simple "Wronnay Search Engine" from 2014 (which is deprecated).

## General Information

License: GNU General Public License

Author: Christoph Daniel Miksche

## Dependencies

The crawler uses BeautifulSoup for handling the html code and MongoEngine for Data-Management.

## Installation

```
pip install wronnay-search-lib
```

### Database

Please install MongoDB first:

On Debian Servers:

```
apt install mongodb
```

Next steps: create a MongoDB Database and edit the wronnay_search_lib/settings.py file.
