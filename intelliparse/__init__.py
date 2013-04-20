import parsers
import electronics

from parsers import parse

def get_parser_families():
    """ Returns all the parsing family names known to intelliparse """
    return parsers.known_parsers.keys()

def get_parser_names(family):
    """ Returns names of all the available parsers in a family """
    family_parser = parsers.known_parsers.get(family)
    if family_parser is not None:
        return family_parser.keys()
    else:
        raise Exception('Unknown Parser Family "%s"' % family)

def get_family_parser(family):
    if family in parsers.known_parsers:
        return parsers.ParsingHelper(family)
    else:
        raise Exception('Unknown Parser Family "%s"' % family)