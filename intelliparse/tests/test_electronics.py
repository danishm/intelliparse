import unittest
from decimal import Decimal
from intelliparse import electronics

class StorageSizeTests(unittest.TestCase):
    
    def test_1(self):
        s=electronics.parseStorageSize('I have a 32 TB disk')
        self.assertEquals(s, Decimal('32768') )
    
    def test_2(self):
        pass


if __name__=="__main__":
    unittest.main()