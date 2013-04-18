import unittest
from decimal import Decimal
from intelliparse import electronics

class StorageSizeTests(unittest.TestCase):
    
    def test_StorageSize(self):

        # Test storage size in the middle of the string
        size=electronics.parseStorageSize('I have a 32 TB disk')
        self.assertEquals(size, Decimal('32768') )

        # Test storage size in the beginning of the string
        size=electronics.parseStorageSize('250 gb drives are the best')
        self.assertEquals(size, Decimal('250') )

        # Test storage size in the end of the string
        size=electronics.parseStorageSize('I wish I had a drive with 50MB.')
        self.assertEquals(size, Decimal('50')/Decimal('1024') )

        # Test not matching in the middle of the string
        size=electronics.parseStorageSize('that drive is at most500 GB more than what I want')
        self.assertIsNone(size)
    
    def test_ScreenSize(self):
        
        size=electronics.parseScreenSize('It has a 13.1" screen');
        self.assertEquals(size, Decimal('13.1') )
        
        size=electronics.parseScreenSize('It has a 9 iNcH screen');
        self.assertEquals(size, Decimal('9') )
        
        size=electronics.parseScreenSize('I really need a screen of size 24inch');
        self.assertEquals(size, Decimal('24') )
        
        size=electronics.parseScreenSize('7" screen is perfect for me');
        self.assertEquals(size, Decimal('7') )
    
    def test_2(self):
        pass


if __name__=="__main__":
    unittest.main()