#!/usr/bin/python3
"""
The Unittest for the Console
"""
import unittest
from unittest.mock import patch
from io import StringIO
from models.base_model import BaseModel
from console import HBNBCommand


class TestHBNBCommandMethods(unittest.TestCase):
    def setUp(self):
        self.console = HBNBCommand()
        self.console.use_rawinput = False  # Disable raw input for testing
        self.mock_stdout = StringIO()
        self.mock_stderr = StringIO()

    def tearDown(self):
        self.mock_stdout.close()
        self.mock_stderr.close()

    def test_do_create_valid(self):
        with patch('sys.stdout', self.mock_stdout), \
             patch('sys.stderr', self.mock_stderr):
            # Valid create command for BaseModel
            self.console.onecmd("create BaseModel")
            output = self.mock_stdout.getvalue().strip()
            self.assertTrue(len(output) == 36)  # Check for UUID format

    def test_do_create_invalid_class(self):
        with patch('sys.stdout', self.mock_stdout), \
             patch('sys.stderr', self.mock_stderr):
            # Invalid class name
            self.console.onecmd("create InvalidClass")
            output = self.mock_stdout.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")

    def test_do_create_invalid_parameter_format(self):
        with patch('sys.stdout', self.mock_stdout), \
             patch('sys.stderr', self.mock_stderr):
            # Invalid parameter format
            self.console.onecmd("create BaseModel invalid_param")
            output = self.mock_stdout.getvalue().strip()
            self.assertEqual(output, "** invalid parameter format **")

    def test_do_create_invalid_attribute(self):
        with patch('sys.stdout', self.mock_stdout), \
             patch('sys.stderr', self.mock_stderr):
            # Invalid attribute name for BaseModel
            self.console.onecmd("create BaseModel name=TestName")
            output = self.mock_stdout.getvalue().strip()
            self.assertEqual(output, "** invalid attribute 'name' for class 'BaseModel' **")

    def test_do_show_valid(self):
        with patch('sys.stdout', self.mock_stdout), \
             patch('sys.stderr', self.mock_stderr):
            # Create a BaseModel instance
            self.console.onecmd("create BaseModel")
            # Get its ID from the output
            output = self.mock_stdout.getvalue().strip()
            obj_id = output
            self.mock_stdout.truncate(0)  # Clear the buffer

            # Show the created instance
            self.console.onecmd(f"show BaseModel {obj_id}")
            output = self.mock_stdout.getvalue().strip()
            self.assertTrue(obj_id in output)

    def test_do_show_missing_class(self):
        with patch('sys.stdout', self.mock_stdout), \
             patch('sys.stderr', self.mock_stderr):
            # Missing class name
            self.console.onecmd("show")
            output = self.mock_stdout.getvalue().strip()
            self.assertEqual(output, "** class name missing **")

    def test_do_show_class_not_exist(self):
        with patch('sys.stdout', self.mock_stdout), \
             patch('sys.stderr', self.mock_stderr):
            # Class does not exist
            self.console.onecmd("show InvalidClass")
            output = self.mock_stdout.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")

    def test_do_show_missing_id(self):
        with patch('sys.stdout', self.mock_stdout), \
             patch('sys.stderr', self.mock_stderr):
            # Missing object ID
            self.console.onecmd("show BaseModel")
            output = self.mock_stdout.getvalue().strip()
            self.assertEqual(output, "** instance id missing **")

    def test_do_show_instance_not_found(self):
        with patch('sys.stdout', self.mock_stdout), \
             patch('sys.stderr', self.mock_stderr):
            # Object ID does not exist
            self.console.onecmd("show BaseModel 12345")
            output = self.mock_stdout.getvalue().strip()
            self.assertEqual(output, "** no instance found **")

    def test_do_destroy_valid(self):
        with patch('sys.stdout', self.mock_stdout), \
             patch('sys.stderr', self.mock_stderr):
            # Create a BaseModel instance
            self.console.onecmd("create BaseModel")
            # Get its ID from the output
            output = self.mock_stdout.getvalue().strip()
            obj_id = output
            self.mock_stdout.truncate(0)  # Clear the buffer

            # Destroy the created instance
            self.console.onecmd(f"destroy BaseModel {obj_id}")
            output = self.mock_stdout.getvalue().strip()
            self.assertEqual(output, "")

    def test_do_destroy_missing_class(self):
        with patch('sys.stdout', self.mock_stdout), \
             patch('sys.stderr', self.mock_stderr):
            # Missing class name
            self.console.onecmd("destroy")
            output = self.mock_stdout.getvalue().strip()
            self.assertEqual(output, "** class name missing **")

    def test_do_destroy_class_not_exist(self):
        with patch('sys.stdout', self.mock_stdout), \
             patch('sys.stderr', self.mock_stderr):
            # Class does not exist
            self.console.onecmd("destroy InvalidClass")
            output = self.mock_stdout.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")

    def test_do_destroy_missing_id(self):
        with patch('sys.stdout', self.mock_stdout), \
             patch('sys.stderr', self.mock_stderr):
            # Missing object ID
            self.console.onecmd("destroy BaseModel")
            output = self.mock_stdout.getvalue().strip()
            self.assertEqual(output, "** instance id missing **")

    def test_do_destroy_instance_not_found(self):
        with patch('sys.stdout', self.mock_stdout), \
             patch('sys.stderr', self.mock_stderr):
            # Object ID does not exist
            self.console.onecmd("destroy BaseModel 12345")
            output = self.mock_stdout.getvalue().strip()
            self.assertEqual(output, "** no instance found **")

    def test_do_all_valid(self):
        with patch('sys.stdout', self.mock_stdout), \
             patch('sys.stderr', self.mock_stderr):
            # Create two BaseModel instances
            self.console.onecmd("create BaseModel")
            self.console.onecmd("create BaseModel")
            # Get their IDs from the output
            output = self.mock_stdout.getvalue().strip()
            obj_ids = output.split('\n')
            self.mock_stdout.truncate(0)  # Clear the buffer

            # List all BaseModel instances
            self.console.onecmd("all BaseModel")
            output = self.mock_stdout.getvalue().strip()
            for obj_id in obj_ids:
                self.assertTrue(obj_id in output)

    def test_do_all_missing_class(self):
        with patch('sys.stdout', self.mock_stdout), \
             patch('sys.stderr', self.mock_stderr):
            # Missing class name
            self.console.onecmd("all")
            output = self.mock_stdout.getvalue().strip()
            self.assertEqual(output, "** class name missing **")

    def test_do_all_class_not_exist(self):
        with patch('sys.stdout', self.mock_stdout), \
             patch('sys.stderr', self.mock_stderr):
            # Class does not exist
            self.console.onecmd("all InvalidClass")
            output = self.mock_stdout.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")

    def test_do_count_valid(self):
        with patch('sys.stdout', self.mock_stdout), \
             patch('sys.stderr', self.mock_stderr):
            # Create two BaseModel instances
            self.console.onecmd("create BaseModel")
            self.console.onecmd("create BaseModel")
            # Get their IDs from the output
            output = self.mock_stdout.getvalue().strip()
            obj_ids = output.split('\n')
            self.mock_stdout.truncate(0)  # Clear the buffer

            # Count the number of BaseModel instances
            self.console.onecmd("count BaseModel")
            output = self.mock_stdout.getvalue().strip()
            self.assertEqual(output, "2")

    def test_do_count_missing_class(self):
        with patch('sys.stdout', self.mock_stdout), \
             patch('sys.stderr', self.mock_stderr):
            # Missing class name
            self.console.onecmd("count")
            output = self.mock_stdout.getvalue().strip()
            self.assertEqual(output, "** class name missing **")

    def test_do_count_class_not_exist(self):
        with patch('sys.stdout', self.mock_stdout), \
             patch('sys.stderr', self.mock_stderr):
            # Class does not exist
            self.console.onecmd("count InvalidClass")
            output = self.mock_stdout.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")

    def test_do_update_valid(self):
        with patch('sys.stdout', self.mock_stdout), \
             patch('sys.stderr', self.mock_stderr):
            # Create a BaseModel instance
            self.console.onecmd("create BaseModel")
            # Get its ID from the output
            output = self.mock_stdout.getvalue().strip()
            obj_id = output
            self.mock_stdout.truncate(0)  # Clear the buffer

            # Update the created instance
            self.console.onecmd(f"update BaseModel {obj_id} name = 'NewName'")
            output = self.mock_stdout.getvalue().strip()
            self.assertEqual(output, "")

            # Show the updated instance
            self.console.onecmd(f"show BaseModel {obj_id}")
            output = self.mock_stdout.getvalue().strip()
            self.assertTrue("NewName" in output)

    def test_do_update_missing_class(self):
        with patch('sys.stdout', self.mock_stdout), \
             patch('sys.stderr', self.mock_stderr):
            # Missing class name
            self.console.onecmd("update")
            output = self.mock_stdout.getvalue().strip()
            self.assertEqual(output, "** class name missing **")

    def test_do_update_class_not_exist(self):
        with patch('sys.stdout', self.mock_stdout), \
             patch('sys.stderr', self.mock_stderr):
            # Class does not exist
            self.console.onecmd("update InvalidClass 12345 name='NewName'")
            output = self.mock_stdout.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")

    def test_do_update_missing_id(self):
        with patch('sys.stdout', self.mock_stdout), \
             patch('sys.stderr', self.mock_stderr):
            # Missing object ID
            self.console.onecmd("update BaseModel")
            output = self.mock_stdout.getvalue().strip()
            self.assertEqual(output, "** instance id missing **")

    def test_do_update_instance_not_found(self):
        with patch('sys.stdout', self.mock_stdout), \
             patch('sys.stderr', self.mock_stderr):
            # Object ID does not exist
            self.console.onecmd("update BaseModel 12345 name='NewName'")
            output = self.mock_stdout.getvalue().strip()
            self.assertEqual(output, "** no instance found **")

    def test_do_update_missing_attribute(self):
        with patch('sys.stdout', self.mock_stdout), \
             patch('sys.stderr', self.mock_stderr):
            # Missing attribute
            self.console.onecmd("create BaseModel")
            obj_id = self.mock_stdout.getvalue().strip()
            self.mock_stdout.truncate(0)  # Clear the buffer
            self.console.onecmd(f"update BaseModel {obj_id}")
            output = self.mock_stdout.getvalue().strip()
            self.assertEqual(output, "** attribute name missing **")

    def test_do_update_missing_value(self):
        with patch('sys.stdout', self.mock_stdout), \
             patch('sys.stderr', self.mock_stderr):
            # Missing value
            self.console.onecmd("create BaseModel")
            obj_id = self.mock_stdout.getvalue().strip()
            self.mock_stdout.truncate(0)  # Clear the buffer
            self.console.onecmd(f"update BaseModel {obj_id} name=")
            output = self.mock_stdout.getvalue().strip()
            self.assertEqual(output, "** value missing **")

    def test_do_update_invalid_attribute(self):
        with patch('sys.stdout', self.mock_stdout), \
             patch('sys.stderr', self.mock_stderr):
            # Invalid attribute for BaseModel
            self.console.onecmd("create BaseModel")
            obj_id = self.mock_stdout.getvalue().strip()
            self.mock_stdout.truncate(0)  # Clear the buffer
            self.console.onecmd(f"update BaseModel {obj_id} invalid_attr='NewValue'")
            output = self.mock_stdout.getvalue().strip()
            self.assertEqual(output, "** invalid attribute 'invalid_attr' for class 'BaseModel' **")

    def test_do_update_valid_with_kwargs(self):
        with patch('sys.stdout', self.mock_stdout), \
             patch('sys.stderr', self.mock_stderr):
            # Create a BaseModel instance
            self.console.onecmd("create BaseModel")
            # Get its ID from the output
            output = self.mock_stdout.getvalue().strip()
            obj_id = output
            self.mock_stdout.truncate(0)  # Clear the buffer

            # Update the created instance using kwargs
            self.console.onecmd(f"update BaseModel {obj_id} name='NewName' age=25 city='NewCity'")
            output = self.mock_stdout.getvalue().strip()
            self.assertEqual(output, "")

            # Show the updated instance
            self.console.onecmd(f"show BaseModel {obj_id}")
            output = self.mock_stdout.getvalue().strip()
            self.assertTrue("NewName" in output)
            self.assertTrue("age" not in output)
            self.assertTrue("city" not in output)

    def test_do_create_help(self):
        with patch('sys.stdout', self.mock_stdout), \
             patch('sys.stderr', self.mock_stderr):
            self.console.onecmd("help create")
            output = self.mock_stdout.getvalue().strip()
            self.assertTrue("Create an object of any class" in output)
            self.assertTrue("Usage: create <className> [<key1=value1> <key2=value2> ...]" in output)

    def test_do_show_help(self):
        with patch('sys.stdout', self.mock_stdout), \
             patch('sys.stderr', self.mock_stderr):
            self.console.onecmd("help show")
            output = self.mock_stdout.getvalue().strip()
            self.assertTrue("Method to show an individual object" in output)
            self.assertTrue("[Usage]: show <className> <objectId>" in output)

    def test_do_destroy_help(self):
        with patch('sys.stdout', self.mock_stdout), \
             patch('sys.stderr', self.mock_stderr):
            self.console.onecmd("help destroy")
            output = self.mock_stdout.getvalue().strip()
            self.assertTrue("Destroys an individual instance of a class" in output)
            self.assertTrue("[Usage]: destroy <className> <objectId>"
                    in output)

    def test_do_all_help(self):
        with patch('sys.stdout', self.mock_stdout), \
             patch('sys.stderr', self.mock_stderr):
            self.console.onecmd("help all")
            output = self.mock_stdout.getvalue().strip()
            self.assertTrue("Shows all objects, or all objects of a class"
                    in output)
            self.assertTrue("[Usage]: all <className>" in output)

    def test_do_count_help(self):
        with patch('sys.stdout', self.mock_stdout), \
             patch('sys.stderr', self.mock_stderr):
            self.console.onecmd("help count")
            output = self.mock_stdout.getvalue().strip()
            self.assertTrue("Count current number of class instances"
                    in output)
            self.assertTrue("Usage: count <class_name>" in output)

    def test_do_update_help(self):
        with patch('sys.stdout', self.mock_stdout), \
             patch('sys.stderr', self.mock_stderr):
            self.console.onecmd("help update")
            output = self.mock_stdout.getvalue().strip()
            self.assertTrue("Updates an object with new information" in output)
            self.assertTrue(
                    "Usage: update < className > < id > < attName > < attVal >"
                    in output)


if __name__ == "__main__":
    unittest.main()
