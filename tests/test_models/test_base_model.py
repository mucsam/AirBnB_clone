#!/usr/bin/python3
"""Testing the base model for Airbnb clone
"""
import unittest
from models.base_model import BaseModel
import uuid
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """Class to test the base model"""

    def setUp(self):
        """Define instructions that will be executed before
        each test method
        """
        self.obj1 = BaseModel()

    def tearDown(self):
        """Define instructions that will be executed after each test method
        """
        pass

    def test_id(self):
        """Tests the id of the BaseModel objects"""

        self.assertNotEqual(self.obj1.id, str(uuid.uuid4()))

    def test_basic(self):
        self.obj1.name = "Samuel"
        self.assertEqual(self.obj1.name, "Samuel")

if __name__ == '__main__':
    unittest.main()
