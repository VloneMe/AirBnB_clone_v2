#!/usr/bin/python3
""" """
#!/usr/bin/python3
""" """
import unittest
from models.user import User
from models.base_model import BaseModel


class test_user(unittest.TestCase):
    def setUp(self):
        """Set up for the test"""
        self.user = User()

    def tearDown(self):
        """Clean up after the test"""
        del self.user

    def test_user_inherits_from_base_model(self):
        """Test if User inherits from BaseModel"""
        self.assertIsInstance(self.user, BaseModel)

    def test_attributes(self):
        """Test User attributes"""
        self.assertTrue(hasattr(self.user, 'email'))
        self.assertTrue(hasattr(self.user, 'password'))
        self.assertTrue(hasattr(self.user, 'first_name'))
        self.assertTrue(hasattr(self.user, 'last_name'))

    def test_email_attribute(self):
        """Test if email is a string"""
        self.assertEqual(type(self.user.email), str)

    def test_password_attribute(self):
        """Test if password is a string"""
        self.assertEqual(type(self.user.password), str)

    def test_first_name_attribute(self):
        """Test if first_name is a string"""
        self.assertEqual(type(self.user.first_name), str)

    def test_last_name_attribute(self):
        """Test if last_name is a string"""
        self.assertEqual(type(self.user.last_name), str)

    def test_places_relationship(self):
        """Test the places relationship"""
        self.assertTrue(hasattr(self.user, 'places'))
        self.assertEqual(type(self.user.places), list)

    def test_reviews_relationship(self):
        """Test the reviews relationship"""
        self.assertTrue(hasattr(self.user, 'reviews'))
        self.assertEqual(type(self.user.reviews), list)

    def test_to_dict_method(self):
        """Test the to_dict method of User"""
        user_dict = self.user.to_dict()
        self.assertEqual(type(user_dict), dict)
        self.assertIn('id', user_dict)
        self.assertIn('created_at', user_dict)
        self.assertIn('updated_at', user_dict)
        self.assertIn('email', user_dict)
        self.assertIn('password', user_dict)
        self.assertIn('first_name', user_dict)
        self.assertIn('last_name', user_dict)

    def test_str_representation(self):
        """Test the __str__ method of User"""
        self.assertEqual(str(self.user), "[User] ({}) {}".format(
            self.user.id, self.user.__dict__))


if __name__ == '__main__':
    unittest.main()
