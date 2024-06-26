#!/usr/bin/python3
"""
classes TestDBStorageDocs and TestDBStorage.
"""
from models.engine import db_storage
from datetime import datetime
import inspect
import json
import models
from models.amenity import Amenity
import unittest
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import os
import pycodestyle

DBStorage = db_storage.DBStorage
classes = {"Amenity": Amenity, "City": City, "Place": Place,
           "Review": Review, "State": State, "User": User}
storage_t = os.getenv("HBNB_TYPE_STORAGE")


class TestDBStorageDocs(unittest.TestCase):
    """ check the documentation of DBStorage """
    @classmethod
    def setUpClass(cls):
        """Set-up for tests"""
        cls.dbs_f = inspect.getmembers(DBStorage, inspect.isfunction)

    def test_pep8_conformance_db_storage(self):
        """Test for conformity to PEP8."""
        pep8s = pycodestyle.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/engine/db_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_db_storage(self):
        """Test conformity to PEP8."""
        pep8s = pycodestyle.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_engine/\
test_db_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")


# class TestFileStorage(unittest.TestCase):
#     """Tes FileStorage"""
#     @unittest.skipIf(storage_t != 'db', "not testing db storage")
#     def test_all_returns_dict(self):
#         """Test for returning a dictionaty"""
#         self.assertIs(type(models.storage.all()), dict)

#     @unittest.skipIf(storage_t != 'db', "not testing db storage")
#     def test_all_no_class(self):
#         """Testing for return of rows"""

#     @unittest.skipIf(storage_t != 'db', "not testing db storage")
#     def test_new(self):
#         """ """

#     @unittest.skipIf(storage_t != 'db', "not testing db storage")
#     def test_save(self):
#         """ saving objects to file.json"""

class TestDBStorageDocs(unittest.TestCase):
    """checking documentation of DBStorage """
    @classmethod
    def setUpClass(cls):
        """Set up for tests"""
        cls.dbs_f = inspect.getmembers(DBStorage, inspect.isfunction)

    def test_pep8_conformance_db_storage(self):
        """Test conformity to PEP8."""
        pep8s = pycodestyle.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/engine/db_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_db_storage(self):
        """Test conformity to PEP8."""
        pep8s = pycodestyle.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_engine/\
test_db_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_db_storage_module_docstring(self):
        """Test docstring"""
        self.assertIsNot(db_storage.__doc__, None,
                         "db_storage.py needs a docstring")
        self.assertTrue(len(db_storage.__doc__) >= 1,
                        "db_storage.py needs a docstring")

    def test_db_storage_class_docstring(self):
        """Test docstring"""
        self.assertIsNot(DBStorage.__doc__, None,
                         "DBStorage class needs a docstring")
        self.assertTrue(len(DBStorage.__doc__) >= 1,
                        "DBStorage class needs a docstring")

    def test_dbs_func_docstrings(self):
        """ """
        for func in self.dbs_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestFileStorage(unittest.TestCase):
    """ """
    @unittest.skipIf(storage_t != 'db', "not testing db storage")
    def test_all_returns_dict(self):
        """ """
        self.assertIs(type(models.storage.all()), dict)

    @unittest.skipIf(storage_t != 'db', "not testing db storage")
    def test_all_no_class(self):
        """ """

    @unittest.skipIf(storage_t != 'db', "not testing db storage")
    def test_new(self):
        """ """

    @unittest.skipIf(storage_t != 'db', "not testing db storage")
    def test_save(self):
        """ """
