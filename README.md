IntelliParse
============

A Python library to help parse product properties from simple English text, while providing a few constructs and annotation to extend the library with more parsers. The primary motiviation behind this library currently is to be able to extract basic technical information from plain text.

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

The discovery API allows one to programatically explore all the parser families and parsers that intelliparse knows about and to use them dynamically.

	>>> import intelliparse
	>>> intelliparse.get_parser_families()
	['electronics']
	>>> intelliparse.get_parser_names('electronics')
	['mega_pixels', 'connectors', 'screen_size', 'storage_size', 'zoom']

How to parse screen size from arbitrary text

	>>> intelliparse.parse('electronics', 'screen_size', 'I have 11 inch tablet')
	Decimal('11')

Parse all electronics properties dynamically from a piece of text

	>>> electronics=intelliparse.get_family_parser('electronics')
	>>> electronics.parse_all('I have a 32 GB tablet with a 7.1 inch screen')
	{'screen_size': Decimal('7.1'), 'storage_size': Decimal('32.0')}