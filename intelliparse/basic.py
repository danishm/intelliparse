"""
basic.py

A python modeule to include some basic property parsers that may get included
in various families of parsers.
"""

COLORS_TO_PARSE = ['Black', 'White', 'Red', 'Blue', 'Pink']

def parse_color(text):
    
    for color in COLORS_TO_PARSE:
        if color.upper() in text.upper():
            return color
