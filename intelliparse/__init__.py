import sys
import traceback
from parsers import Parser, parser_to_json
import electronics

def parse(name, text):
	'''
	Parse a specific property from text
	'''
	return Parser.parse(name, text)

def parse_all(names, text):
	'''
	Parse a list of properties from text
	@returns dict
	'''
	result={}
	for name in names:
		result[name]=parse(name, text)

	return result

def get_catalogue():
	catalogue={}

	parsers = Parser.get_parsers()
	for name, parser in parsers.iteritems():
		catalogue[parser.name]=parser_to_json(parser)

	return catalogue

def get_parser_into(name):	

	parser = Parser.get_parser(name)
	if parser is not None:
		return parser_to_json(parser)
	else:
		return None

def render(name, value):
	'''
	Render a property value for display
	'''
	return Parser.render(name, value)




print get_catalogue()