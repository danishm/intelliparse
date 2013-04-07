import unittest
from decimal import Decimal
from intelliparse import electronics

class StorageSizeTests(unittest.TestCase):
    
    def test_StorageSize(self):

    	# Test storage size in the middle of the string
        size=electronics.parseStorageSize('I have a 32 TB disk')
        self.assertEquals(size, Decimal('32768') )

        # Test storate size in the begining of the string
        size=electronics.parseStorageSize('250 gb drives are the best')
        self.assertEquals(size, Decimal('250') )

        # Test storate size in the end of the string
        size=electronics.parseStorageSize('I wish I had a drive with 50MB.')
        self.assertEquals(size, Decimal('50')/Decimal('1024') )

        # Test not mactching in the middle of the string
        size=electronics.parseStorageSize('that drive is at most500 GB more than what I want')
        self.assertIsNone(size)

    
    def test_2(self):
        pass


if __name__=="__main__":
    unittest.main()