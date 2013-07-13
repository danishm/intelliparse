
# .------------------------.
# | Decorator Support      |
# '========================'

def parser_to_json(parser):
	return {'name':parser.name, 'label':parser.label}

class Parser(object):
	"""
	A decorator to mark a parser function with a family and a
	custom name. If a name is not provided, the name is derived
	from the function name it sarts with 'parse' e.g. if the
	function name is 'parseStorageSize' then the parser name is
	'storageSize'
	"""
	
	parsers={}
	
	def __init__(self):
		pass

	def __call__(self, parser):
		self.parsers[parser.name] = parser()
		return parser

	@classmethod
	def get_parsers(cls):
		return cls.parsers

	@classmethod
	def get_parser(cls, name):
		return cls.parsers.get(name)

	@classmethod
	def parse(cls, name, text):
		parser = cls.get_parser(name)
		if parser is not None:
			return parser.parse(text)
		else:
			return None

	@classmethod
	def render(cls, name, value):
		parser = cls.get_parser(name)
		if parser is not None:
			return parser.render(value)
		else:
			return None

