#!/usr/bin/python3
"""Instantiating an object of class FileStorage"""

from models.engine.db_storage import DBStorage
from os import getenv
from models.engine.file_storage import FileStorage

if getenv('HBNB_TYPE_STORAGE') == 'db':
    storage = DBStorage()
else:
  storage = FileStorage()
storage.reload()
