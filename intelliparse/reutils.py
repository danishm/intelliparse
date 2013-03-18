"""
Module to help with regular expressions
"""
import re
from decimal import Decimal

NUMBER_REGEX = "[-+]?[0-9]*\\.?[0-9]+"

def getMatches(regex, text):
    """
    @summary: Finds and returns all matches of the regex in the text
    
    @param regex: The regex to use
    @type regex: Compiled regex or string
    
    @param text: The text to find matches from
    """
    result=[]
    matches=re.findall(regex, text)
    for match in matches:
        result.append(match)
    
    return result


def getMatch(regex, text):
    matches=getMatches(regex, text)
    if len(matches)>0:
        return matches[0]
    else:
        return None


def extractNumber(text):
    """
    @summary: Extracts a number from a string
    
    @param text: Text to extract the number from
    """
    matches=getMatches(NUMBER_REGEX, text)
    if len(matches)>0:
        return Decimal(matches[0])
    else:
        return None