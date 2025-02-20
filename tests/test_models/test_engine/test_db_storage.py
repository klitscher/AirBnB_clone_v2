#!/usr/bin/python3
""" Unittests for db_storage """
import unittest
import os
import pep8
import MySQLdb
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.db_storage import DBStorage


class TestDBStorage(unittest.TestCase):
    """Tests for SQLAlchemy storage method."""


        db = MySQLdb.connect(host="localhost", user=hbnb_test,
                             passwd=hbnb_test_pwd, db=hbnb_test_db)
        cur = db.cursor()

    @classmethod
    def setUpClass(cls):
        """setup for funsies."""
        cls.user = User()
        cls.user.first_name = "Nate"
        cls.user.last_name = "KittyCat"
        cls.user.email = "murderface@bird.com"
        cls.storage = DBStorage()

    def test_pep8_dbs(self):
        """tests pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/engine/db_storage.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_db_basic(self):
        pass
