#!/usr/bin/python3
""" """
#!/usr/bin/python3
""" """
import unittest
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    def setUp(self):
        """Set up for the test"""
        self.state = State()

    def tearDown(self):
        """Clean up after the test"""
        del self.state

    def test_state_inherits_from_base_model(self):
        """Test if State inherits from BaseModel"""
        self.assertIsInstance(self.state, BaseModel)

    def test_attributes(self):
        """Test State attributes"""
        self.assertTrue(hasattr(self.state, 'name'))

    def test_name_attribute(self):
        """Test if name is a string"""
        self.assertEqual(type(self.state.name), str)

    def test_cities_property(self):
        """Test the cities property"""
        self.assertTrue(hasattr(self.state, 'cities'))
        self.assertEqual(type(self.state.cities), list)

    def test_to_dict_method(self):
        """Test the to_dict method of State"""
        state_dict = self.state.to_dict()
        self.assertEqual(type(state_dict), dict)
        self.assertIn('id', state_dict)
        self.assertIn('created_at', state_dict)
        self.assertIn('updated_at', state_dict)
        self.assertIn('name', state_dict)

    def test_str_representation(self):
        """Test the __str__ method of State"""
        self.assertEqual(str(self.state), "[State] ({}) {}".format(
            self.state.id, self.state.__dict__))


if __name__ == '__main__':
    unittest.main()
