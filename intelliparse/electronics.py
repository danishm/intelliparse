"""
electronics.py

Module to help with parsing of properties of typical electronic gadgets
available in the market e.g. Tables, Flash Drives, Camera etc
"""
import reutils
from decimal import Decimal

K   = Decimal('1024.0')
ONE = Decimal('1.0')

STORAGE_SIZE_PREGEX         = ' ([0-9,.]+) ?([K, M, G, T]B)[ ,.]'
STORAGE_SIZE_UNIT_REGEX     = '[K, M, G, T]B'

SCREEN_SIZE_REGEX           = '(\\d+\\.?\\d*) ?(INCH|")'

MEGA_PIXEL_REGEX            = '(\\d+\\.?\\d*)[ ,-]?()'

CONNECTORS_REGEX_MAP        = {'USB 1': 'USB[ |-]?1',
                                'USB 2.0': 'USB[ |-]?2(.0)?',
                                'USB 3.0': 'USB[ |-]?3(.0)?'}

ZOOM_REGEX                  = '(\\d+\\.?\\d*)[x|X]'

STORAGE_SIZE_MULTIPLIERS = {
    'KB': ONE/(K*K),
    'MB': ONE/K,
    'GB': ONE,
    'TB': K
}

def parseStorageSizeUnit(text):
    """Extract the unit of storage e.g. MB, GB etc."""
    return reutils.getMatch(STORAGE_SIZE_UNIT_REGEX, text.upper())
    
def parseStorageSize(text):
    """Parse Storage Size from text"""
    match=reutils.getMatch(STORAGE_SIZE_PREGEX, text.upper())
    if match is not None:
        size=Decimal(match[0])
        unit=match[1]
        print 'Found', size, unit
        if unit in STORAGE_SIZE_MULTIPLIERS:
            return size*STORAGE_SIZE_MULTIPLIERS[unit]
    return None


def parseScreenSize(text):
    """Parse ScreenSize from text"""
    match=reutils.getMatch(SCREEN_SIZE_REGEX, text.upper())
    if match is not None:
        size=Decimal(match[0])
        return size
        
    return None


def parseMegaPixels(text):
    """Parse Mega Pixels from text"""
    match=reutils.getMatch(MEGA_PIXEL_REGEX, text.upper())
    if match is not None:
        mp=Decimal(match[0])
        return mp
        
    return None

def parseConnectors(text):
    """Parse connectors available on the device"""
    return reutils.getEnumMatches(CONNECTORS_REGEX_MAP, text.upper())

def parseZoom(text):
    """Parse Zoom from text"""
    match=reutils.getMatch(ZOOM_REGEX, text.upper())
    if match is not None:
        size=Decimal(match)
        return size
        
    return None
    
print parseZoom('I have a 32x digital camera')
