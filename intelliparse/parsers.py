ELECTRONICS='electronics'

# .------------------------.
# | Known Parsers Library  |
# '========================'

# Stores all the parsers annotated by the @parser decorator
# Its a dict of dict { family: {parserName: parseFunction}}
knownParsers={}

def addKnownParser(family, name, function):
	familyParsers=knownParsers.get(family)
	if familyParsers is None:
		familyParsers={}
		knownParsers[family]=familyParsers

	familyParsers[name]=function


def extractNameFromParser(funcName):
	"""
	Extrats a name from a parser function. It expects the name
	to start with 'parse' with the remaining name in camel case.
	"""
	if funcName.startswith('parse'):
		name=funcName.replace('parse', '')
		name=name[0].lower()+name[1:]
	else:
		name=funcName
	return name


def getParserNames(family):
	familyParsers=knownParsers.get(family)
	if familyParsers is not None:
		return familyParsers.keys()


def parse(family, name, text):
	familyParsers=knownParsers.get(family)
	if familyParsers is not None:
		parser=familyParsers[name]
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
		if self.name==None: self.name=extractNameFromParser(func.__name__)
		addKnownParser(self.family, self.name, func)
		def wrapper(*args, **kwargs):
			return func(*args, **kwargs)

		return wrapper


class ParsingHelper(object):

	def __init__(self, family):
		self.family=family

	def parse(self, name, text):
		return parse(self.family, name, text)

	def parseAll(self, text):
		results={}
		familyParsers=knownParsers[self.family]
		if familyParsers is not None:
			for name in familyParsers:
				parser=familyParsers[name]
				result=parser(text)
				if result is not None:
					results[name]=result
		return results



def getParser(family):
	return ParsingHelper(family)
