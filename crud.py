#!/usr/bin/env python
from pymongo import MongoClient
from bson.objectid import ObjectId
class AnimalShelter(object):

    """ CRUD operations for Animal collection in MongoDB """

def __init__(self, username=None, password=None):
    # Initializing the MongoClient. This helps to
     # access the MongoDB databases and collections.
    if username and password:
        self.client = MongoClient('mongodb://%s:%s@localhost:47748/AAC' % ('aacuser', 'admin'))
    else:
        self.client = MongoClient('mongodb://localhost:47748')
    self.database = self.client['AAC']

# Complete this create method to implement the C in CRUD.

def create(self, data):
    if data is not None:
        insert = self.database.animals.insert(data)  # data should be dictionary
        if insert != 0:
            return True
        else:
            return False
    else:
        raise Exception('Nothing to save, because data parameter is empty')


    # Create method to implement the R in CRUD.
def read(self, data):
    if target is not None:
        read_result = list(self.database.animals.find(data,{'_id': False}))
        return read_result
    else:
         # lets the user know there was a problem
        raise Exception('Nothing to search, because the target parameter is empty')
    return False
