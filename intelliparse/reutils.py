"""
Module to help with regular expressions
"""
import re
from decimal import Decimal

NUMBER_REGEX = "[-+]?[0-9]*\\.?[0-9]+"

def get_matches(regex, text):
    """
    @summary: Finds and returns all matches of the regex in the text
    @param regex: The regex to use
    @type regex: Compiled regex or string
    @param text: The text to find matches from
    """
    matches=re.findall(regex, text)
    return matches

def get_match(regex, text):
    """
    @summary: Get a single match of a regex to the text
    @param regex: The regex to use
    @type regex: Compiled regex or string
    @param text: The text to find matches from
    """
    matches=get_matches(regex, text)
    if len(matches)>0:
        return matches[0]
    else:
        return None

def get_enum_matches(regexMap, text):
    """
    @summary: Returns a list of matches from a pre-defined list of 
              enumerated strings and the coresponding regexes
    @param regexMap: a dict of string enums to their regexes
    @type regexMap: dict
    @param text: The text to find matches from
    """
    matches=[]
    for enum in regexMap:
        regex=regexMap[enum]
        if get_match(regex, text) is not None:
            matches.append(enum)
    return matches

def extract_number(text):
    """
    @summary: Extracts a number from a string
    @param text: Text to extract the number from
    """
    matches=get_matches(NUMBER_REGEX, text)
    if len(matches)>0:
        return Decimal(matches[0])
    else:
        return None