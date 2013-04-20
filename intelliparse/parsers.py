ELECTRONICS='electronics'

# .------------------------.
# | Known Parsers Library  |
# '========================'

# Stores all the parsers annotated by the @parser decorator
# Its a dict of dict { family: {parserName: parseFunction}}
known_parsers={}

def add_parser(family, name, function):
	parser_family = known_parsers.get(family)
	if parser_family is None:
		parser_family={}
		known_parsers[family]=parser_family

	parser_family[name]=function


def extract_name_from_function(func_name):
	"""
	Extracts a name from a parser function. It expects the name
	to start with 'parse' with the remaining name in camel case.
	"""
	if func_name.startswith('parse_'):
		name=func_name.replace('parse_', '')
	else:
		name=func_name
	return name


def get_parser_names(family):
	parser_family=known_parsers.get(family)
	if parser_family is not None:
		return parser_family.keys()


def parse(family, name, text):
	parser_family=known_parsers.get(family)
	if parser_family is not None:
		parser=parser_family[name]
		if parser is not None:
			return parser(text)

# .------------------------.
# | Decorator Support      |
# '========================'

class parser(object):
	"""
	A decorator to mark a parser function with a family and a
	custom name. If a name is not provided, the name is derived
	from the function name it sarts with 'parse' e.g. if the
	function name is 'parseStorageSize' then the parser name is
	'storageSize'
	"""

	def __init__(self, family, name=None):
		self.family=family
		self.name=name

	def __call__(self, func):
		if self.name==None: self.name=extract_name_from_function(func.__name__)
		add_parser(self.family, self.name, func)
		def wrapper(*args, **kwargs):
			return func(*args, **kwargs)

		return wrapper


class ParsingHelper(object):

	def __init__(self, family):
		self.family=family

	def parse(self, name, text):
		return parse(self.family, name, text)

	def parse_all(self, text):
		results={}
		parser_family=known_parsers[self.family]
		if parser_family is not None:
			for name in parser_family:
				parser=parser_family[name]
				result=parser(text)
				if result is not None:
					results[name]=result
		return results


def get_parser_family(family):
	return ParsingHelper(family)
