#!/usr/bin/python3

import unittest
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):

    def setUp(self):
        """Set up for the tests"""
        self.my_amenity = Amenity()
        self.my_amenity.name = "Pool"

    def test_attributes(self):
        """Test the attributes of Amenity"""
        amenity = Amenity
        self.assertIsInstance(amenity, Amenity)
        self.assertEqual(amenity.name, "")

if __name__ == '__main__':
    unittest.main()
