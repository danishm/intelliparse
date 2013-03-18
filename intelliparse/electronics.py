"""
electronics.py

Module to help with parsing of properties of typical electronic gadgets
available in the market e.g. Tables, Flash Drives, Camera etc
"""
import reutils
from decimal import Decimal

K   = Decimal('1024.0')
ONE = Decimal('1.0')

STORAGE_SIZE_PREGEX         = ' ([0-9,.]+ ?[K, M, G, T]B)[ ,.]'
STORAGE_SIZE_UNIT_REGEX     = '[K, M, G, T]B'

STORAGE_SIZE_MULTIPLIERS = {
    'KB': ONE/(K*K),
    'MB': ONE/K,
    'GB': ONE,
    'TB': K
}

def parseStorageSizeUnit(text):
    return reutils.getMatch(STORAGE_SIZE_UNIT_REGEX, text.upper())
    
def parseStorageSize(text):
    match=reutils.getMatch(STORAGE_SIZE_PREGEX, text.upper())
    if match is not None:
        size=reutils.extractNumber(match)
        unit=parseStorageSizeUnit(match)
        if unit in STORAGE_SIZE_MULTIPLIERS:
            return size*STORAGE_SIZE_MULTIPLIERS[unit]
        else:
            return None
    else:
        return None



print parseStorageSize('A flash drive with 32MB storage')
