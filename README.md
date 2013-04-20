IntelliParse
============

A Python library to help parse product properties from simple English text, while providing a few constructs and annotation to extend the library with more parsers.

Installation
------------
The current installation process is to simple clone the repository and use the distutils to install

	git clone https://github.com/danishm/intelliparse.git
	cd intelliparse
	sudo python setup.py install

Usage
-----

### Explicit API

The explicit API is used to explicitly parse a specific property of a specific family of products. For discovery through meta-data and parsing of all properties at once for a given product family, please take a look at the discoverable API

	>>> from intelliparse import electronics
	>>> electronics.parse_storage_size('QuickDrive 32 GB Flash Drive')
	Decimal('32.0')	
	>>>	electronics.parse_screen_size('Here is a 11 inch tablet')
	Decimal('11')

### Discovery API

Comming soon