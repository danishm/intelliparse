import sys
import traceback
import parsers
import electronics

from parsers import parse, parse_all

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

def enrich(family, properties, parse_fields=[]):
    
    try:
        fields = properties.keys() if len(parse_fields)==0 else parse_fields
        parse_blob = ""
        for field in fields:
            value = properties.get(field)
            print field, value
            if value is not None:
                if isinstance(value, basestring):
                    parse_blob = parse_blob + value + " "
        
        enrich_fields = parse_all(family, parse_blob)
        properties.update(enrich_fields)
    except:
        print "Exception trying to enrich '%s' for product:%s" % (family, properties)
        print '-'*60
        traceback.print_exc(file=sys.stdout)
        print '-'*60