ELECTRONICS='electronics'

knownParsers={}

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
		knownParsers[(self.family, self.name)]=func
		def wrapper(*args, **kwargs):
			return func

		return wrapper


def getParserNames(family):
	names=[]
	for key in knownParsers:
		keyfam, name = key
		if family==keyfam:
			names.append(name)
	return names

def parse(family, name, text):
	key=(family, name)
	if key in knownParsers:
		parseFunction=knownParsers[key]
		return parseFunction(text)
	else:
		return None