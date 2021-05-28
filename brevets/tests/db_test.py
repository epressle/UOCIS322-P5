import nose
from pymongo import MongoClient
import os
import logging
from bson.objectid import ObjectId

def test_db_single():
    client = MongoClient('mongodb://' + os.environ['MONGODB_HOSTNAME'], 27017)
    db = client.tempdb

    test_dict_single = {
        'brev_distance': '400',
        'open_times': ['2021-01-01T00:00'],
        'close_times': ['2021-01-01T01:00'],
        'kms': [0]
    }
    client.drop_database('tempdb')

    res = db.tempdb.insert_one(test_dict_single)
    ID = ObjectId(res.inserted_id)
    # check for valid insertion
    assert(res.acknowledged)
    assert(db.tempdb.find_one({'_id': ID}) is not None)
    # delete from database
    assert(db.tempdb.find_one_and_delete({'_id': ID}) is not None)
    assert(db.tempdb.find_one({'_id': ID}) is None)

def test_db_multi():
    client = MongoClient('mongodb://' + os.environ['MONGODB_HOSTNAME'], 27017)
    db = client.tempdb

    test_dict_multi = {
        'brev_distance': '1000',
        'open_times': ['2021-01-01T00:00', '2021-01-01T02:56', '2021-01-01T05:53', '2021-01-01T12:08', '2021-01-01T22:22', '2021-01-02T09:05'],
        'close_times': ['2021-01-01T01:00', '2021-01-01T06:40', '2021-01-01T13:30', '2021-01-02T02:40', '2021-01-03T00:45', '2021-01-04T03:00'],
        'kms': ['0', '100', '200', '400', '700', '1000']
    }
    client.drop_database('tempdb')

    res = db.tempdb.insert_one(test_dict_multi)
    ID = ObjectId(res.inserted_id)
    # check for valid insertion
    assert(res.acknowledged)
    assert(db.tempdb.find_one({'_id': ID}) is not None)
    # delete from database
    assert(db.tempdb.find_one_and_delete({'_id': ID}) is not None)
    assert(db.tempdb.find_one({'_id': ID}) is None)
