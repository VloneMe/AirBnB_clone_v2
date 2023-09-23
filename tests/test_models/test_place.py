#!/usr/bin/python3
""" """
import unittest
from models.place import Place
from models.base_model import BaseModel
from os import getenv


class test_place(unittest.TestCase):
    def setUp(self):
        """Set up for the test"""
        self.place = Place()

    def tearDown(self):
        """Clean up after the test"""
        del self.place

    def test_place_inherits_from_base_model(self):
        """Test if Place inherits from BaseModel"""
        self.assertIsInstance(self.place, BaseModel)

    def test_attributes(self):
        """Test Place attributes"""
        self.assertTrue(hasattr(self.place, 'city_id'))
        self.assertTrue(hasattr(self.place, 'user_id'))
        self.assertTrue(hasattr(self.place, 'name'))
        self.assertTrue(hasattr(self.place, 'description'))
        self.assertTrue(hasattr(self.place, 'number_rooms'))
        self.assertTrue(hasattr(self.place, 'number_bathrooms'))
        self.assertTrue(hasattr(self.place, 'max_guest'))
        self.assertTrue(hasattr(self.place, 'price_by_night'))
        self.assertTrue(hasattr(self.place, 'latitude'))
        self.assertTrue(hasattr(self.place, 'longitude'))
        self.assertTrue(hasattr(self.place, 'amenity_ids'))

    def test_attributes_are_strings(self):
        """Test if city_id, user_id, name, and description are strings"""
        self.assertEqual(type(self.place.city_id), str)
        self.assertEqual(type(self.place.user_id), str)
        self.assertEqual(type(self.place.name), str)
        self.assertEqual(type(self.place.description), str)

    def test_attributes_are_integers(self):
        """Test if number_rooms, number_bathrooms, max_guest, and price_by_night are integers"""
        self.assertEqual(type(self.place.number_rooms), int)
        self.assertEqual(type(self.place.number_bathrooms), int)
        self.assertEqual(type(self.place.max_guest), int)
        self.assertEqual(type(self.place.price_by_night), int)

    def test_attributes_are_floats(self):
        """Test if latitude and longitude are floats"""
        self.assertEqual(type(self.place.latitude), float)
        self.assertEqual(type(self.place.longitude), float)

    def test_reviews_relationship(self):
        """Test the reviews relationship"""
        if getenv("HBNB_TYPE_STORAGE") == "db":
            self.assertTrue(hasattr(self.place, 'reviews'))

    def test_amenities_relationship(self):
        """Test the amenities relationship"""
        if getenv("HBNB_TYPE_STORAGE") == "db":
            self.assertTrue(hasattr(self.place, 'amenities'))

    def test_to_dict_method(self):
        """Test the to_dict method of Place"""
        place_dict = self.place.to_dict()
        self.assertEqual(type(place_dict), dict)
        self.assertIn('id', place_dict)
        self.assertIn('created_at', place_dict)
        self.assertIn('updated_at', place_dict)
        self.assertIn('city_id', place_dict)
        self.assertIn('user_id', place_dict)
        self.assertIn('name', place_dict)
        self.assertIn('description', place_dict)
        self.assertIn('number_rooms', place_dict)
        self.assertIn('number_bathrooms', place_dict)
        self.assertIn('max_guest', place_dict)
        self.assertIn('price_by_night', place_dict)
        self.assertIn('latitude', place_dict)
        self.assertIn('longitude', place_dict)
        self.assertIn('amenity_ids', place_dict)

    def test_str_representation(self):
        """Test the __str__ method of Place"""
        self.assertEqual(str(self.place), "[Place] ({}) {}".format(
            self.place.id, self.place.__dict__))


if __name__ == '__main__':
    unittest.main()
