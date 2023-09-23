#!/usr/bin/python3

#!/usr/bin/python3
""" """
import unittest
from models.city import City
from models.base_model import BaseModel
from os import getenv


class TestCity(unittest.TestCase):
    def setUp(self):
        """Set up for the test"""
        self.city = City()

    def tearDown(self):
        """Clean up after the test"""
        del self.city

    def test_city_inherits_from_base_model(self):
        """Test if City inherits from BaseModel"""
        self.assertIsInstance(self.city, BaseModel)

    def test_attributes(self):
        """Test City attributes"""
        self.assertTrue(hasattr(self.city, 'name'))
        self.assertTrue(hasattr(self.city, 'state_id'))

    def test_attributes_are_strings(self):
        """Test if name and state_id are strings"""
        self.assertEqual(type(self.city.name), str)
        self.assertEqual(type(self.city.state_id), str)

    def test_storage_type(self):
        """Test if the storage_type attribute is set"""
        self.assertTrue(hasattr(self.city, '__tablename__'))

    def test_tablename(self):
        """Test if the __tablename__ attribute is correctly set to 'cities'"""
        self.assertEqual(self.city.__tablename__, 'cities')

    def test_relationship_with_place(self):
        """Test the places relationship"""
        if getenv("HBNB_TYPE_STORAGE") == "db":
            self.assertTrue(hasattr(self.city, 'places'))

    def test_to_dict_method(self):
        """Test the to_dict method of City"""
        city_dict = self.city.to_dict()
        self.assertEqual(type(city_dict), dict)
        self.assertIn('id', city_dict)
        self.assertIn('created_at', city_dict)
        self.assertIn('updated_at', city_dict)
        self.assertIn('name', city_dict)
        self.assertIn('state_id', city_dict)

    def test_str_representation(self):
        """Test the __str__ method of City"""
        self.assertEqual(str(self.city), "[City] ({}) {}".format(
            self.city.id, self.city.__dict__))


if __name__ == '__main__':
    unittest.main()
