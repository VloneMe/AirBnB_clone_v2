#!/usr/bin/python3
""" """
#!/usr/bin/python3
""" """
import unittest
from models.review import Review
from models.base_model import BaseModel


class test_review(unittest.TestCase):
    def setUp(self):
        """Set up for the test"""
        self.review = Review()

    def tearDown(self):
        """Clean up after the test"""
        del self.review

    def test_review_inherits_from_base_model(self):
        """Test if Review inherits from BaseModel"""
        self.assertIsInstance(self.review, BaseModel)

    def test_attributes(self):
        """Test Review attributes"""
        self.assertTrue(hasattr(self.review, 'text'))
        self.assertTrue(hasattr(self.review, 'place_id'))
        self.assertTrue(hasattr(self.review, 'user_id'))

    def test_attributes_are_strings(self):
        """Test if text, place_id, and user_id are strings"""
        self.assertEqual(type(self.review.text), str)
        self.assertEqual(type(self.review.place_id), str)
        self.assertEqual(type(self.review.user_id), str)

    def test_to_dict_method(self):
        """Test the to_dict method of Review"""
        review_dict = self.review.to_dict()
        self.assertEqual(type(review_dict), dict)
        self.assertIn('id', review_dict)
        self.assertIn('created_at', review_dict)
        self.assertIn('updated_at', review_dict)
        self.assertIn('text', review_dict)
        self.assertIn('place_id', review_dict)
        self.assertIn('user_id', review_dict)

    def test_str_representation(self):
        """Test the __str__ method of Review"""
        self.assertEqual(str(self.review), "[Review] ({}) {}".format(
            self.review.id, self.review.__dict__))


if __name__ == '__main__':
    unittest.main()
