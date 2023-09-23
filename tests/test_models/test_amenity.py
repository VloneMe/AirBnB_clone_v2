#!/usr/bin/python3
""" """
import os
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel
from tests.test_models.test_base_model import test_basemodel


class test_Amenity(unittest.TestCase):
    """Test cases for the Amenity class."""

    def test_attribute_types(self):
        """Test attribute types of the Amenity class."""
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, 'name'))
        self.assertEqual(type(amenity.name), str)

    def test_instance_creation(self):
        """Test instance creation of the Amenity class."""
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)
        self.assertEqual(amenity.__class__.__name__, 'Amenity')

    def test_str_representation(self):
        """Test string representation of the Amenity class."""
        amenity = Amenity()
        amenity.name = "WiFi"
        string_representation = str(amenity)
        self.assertIn("[Amenity]", string_representation)
        self.assertIn("'name': 'WiFi'", string_representation)

    def test_to_dict_method(self):
        """Test the to_dict method of the Amenity class."""
        amenity = Amenity()
        amenity.name = "Pool"
        amenity_dict = amenity.to_dict()
        self.assertEqual(type(amenity_dict), dict)
        self.assertIn('name', amenity_dict)
        self.assertEqual(amenity_dict['name'], 'Pool')

    def test_dict_to_instance_creation(self):
        """Test creating an instance from a dictionary of attributes."""
        amenity_data = {
            'id': '123',
            'created_at': '2022-01-01T00:00:00.000000',
            'updated_at': '2022-01-02T00:00:00.000000',
            'name': 'Gym'
        }
        amenity = Amenity(**amenity_data)
        self.assertEqual(amenity.id, '123')
        self.assertEqual(amenity.created_at.isoformat(), '2022-01-01T00:00:00')
        self.assertEqual(amenity.updated_at.isoformat(), '2022-01-02T00:00:00')
        self.assertEqual(amenity.name, 'Gym')


if __name__ == '__main__':
    unittest.main()
