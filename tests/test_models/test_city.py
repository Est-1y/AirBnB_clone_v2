#!/usr/bin/python3
"""test city module """

import pycodestyle
from tests.test_models.test_base_model import test_basemodel
from models.city import City


class test_City(test_basemodel):
    """test city """

    def __init__(self, *args, **kwargs):
        """arguments """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """test state """
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """test name """
        new = self.value()
        self.assertEqual(type(new.name), str)


class Test_PEP8(unittest.TestCase):
    """test User"""

    def test_pep8_user(self):
        """pep8 """
        pep8style = pycodestyle.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/city.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")


class TestCity(unittest.TestCase):
    """test city class X"""

    @classmethod
    def setUpClass(cls):
        """setup t"""
        cls.city = City()
        cls.city.name = "LA"
        cls.city.state_id = "CA"

    @classmethod
    def teardown(cls):
        """ """
        del cls.city

    def tearDown(self):
        """teardown"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_City(self):
        """pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/city.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_checking_for_docstring_City(self):
        """docstrings"""
        self.assertIsNotNone(City.__doc__)

    def test_attributes_City(self):
        """checking for attributes"""
        self.assertTrue('id' in self.city.__dict__)
        self.assertTrue('created_at' in self.city.__dict__)
        self.assertTrue('updated_at' in self.city.__dict__)
        self.assertTrue('state_id' in self.city.__dict__)
        self.assertTrue('name' in self.city.__dict__)

    def test_is_subclass_City(self):
        """test if City is a subclass"""
        self.assertTrue(issubclass(self.city.__class__, BaseModel), True)

    def test_attribute_types_City(self):
        """attribute type"""
        self.assertEqual(type(self.city.name), str)
        self.assertEqual(type(self.city.state_id), str)

    def test_save_City(self):
        """test save"""
        self.city.save()
        self.assertNotEqual(self.city.created_at, self.city.updated_at)

    def test_to_dict_City(self):
        """test dictionary"""
        self.assertEqual('to_dict' in dir(self.city), True)


if __name__ == "__main__":
    unittest.main()
