"""
electronics.py

Module to help with parsing of properties of typical electronic gadgets
available in the market e.g. Tables, Flash Drives, Camera etc
"""
import reutils
import utils
from parsers import Parser

K   = utils.to_float('1024.0')
ONE = utils.to_float('1.0')

STORAGE_SIZE_PREGEX         = '\\b([0-9,.]+) ?([K, M, G, T]B)[ ,.]'
STORAGE_SIZE_UNIT_REGEX     = '[K, M, G, T]B'

SCREEN_SIZE_REGEX           = '(\\d+\\.?\\d*) ?(INCH|")'

MEGA_PIXEL_REGEX            = '(\\d+\\.?\\d*)[ ,-]?(MP|MEGAPIXEL)'

CONNECTORS_REGEX_MAP        = { 'USB 1': 'USB[ |-]?1',
                                'USB 2.0': 'USB[ |-]?2(.0)?',
                                'USB 3.0': 'USB[ |-]?3(.0)?'}

ZOOM_REGEX                  = '(\\d+\\.?\\d*)[x|X]'

STORAGE_SIZE_MULTIPLIERS = {
    'KB': ONE/(K*K),
    'MB': ONE/K,
    'GB': ONE,
    'TB': K
}

@Parser()
class StorageSizeParser(object):
    name = 'storage_size'
    label = 'Storage Size'
    
    def parse(self, text):
        """Parse Storage Size from text"""
        match=reutils.get_match(STORAGE_SIZE_PREGEX, text.upper())
        if match is not None:
            size=utils.to_float(match[0])
            unit=match[1]
            if unit in STORAGE_SIZE_MULTIPLIERS:
                return size*STORAGE_SIZE_MULTIPLIERS[unit]
        return None
    
    def render(self, value):
        return '%s GB' % value


@Parser()
class ScreenSizeParser(object):
    name = "screen_size"
    label = "Screen Size"
    
    def parse(self, text):
        """Parse ScreenSize from text"""
        match=reutils.get_match(SCREEN_SIZE_REGEX, text.upper())
        if match is not None:
            size=utils.to_float(match[0])
            return size
            
        return None
    
    def render(self, value):
        return '%s"' % value


@Parser()
class MegaPixelsParser(object):
    name = "mega_pixels"
    label = "Mega Pixels"
    
    def parse(self, text):
        """Parse Mega Pixels from text"""
        match=reutils.get_match(MEGA_PIXEL_REGEX, text.upper())
        if match is not None:
            mp=utils.to_float(match[0])
            return mp
            
        return None
    
    def render(self, value):
        return '%s MP' % value


@Parser()
class ConnectorsParser(object):
    name = "connectors"
    label = "Connectors"
    
    def parse(self, text):
        """Parse connectors available on the device"""
        matches = reutils.get_enum_matches(CONNECTORS_REGEX_MAP, text.upper())
        if len(matches)>0:
            return matches
        else:
            return None
    
    def render(self, value):
        return '%s' % value


@Parser()
class ZoomParser(object):
    name = "zoom"
    label = "Zoom"
    
    def parse(self, text):
        """Parse Zoom from text"""
        match=reutils.get_match(ZOOM_REGEX, text.upper())
        if match is not None:
            size=utils.to_float(match)
            return size
            
        return None
    
    def render(self, value):
        return '%sx' % value
