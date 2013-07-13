
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
	
	parsers={}
	
	def __init__(self):
		pass

	def __call__(self, parser):
		self.parsers[parser.name] = parser()
		return parser

