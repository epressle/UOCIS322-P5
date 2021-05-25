import nose
from pymongo import MongoClient
import os
from flask_brevets import insert_to_db


def test_db_single():
    client = MongoClient('mongodb://' + os.environ['MONGODB_HOSTNAME'], 27017)
    db = client.brevetdb

    test_dict_single = {
        'brev_distance': '400',
        'open_times': ['2021-01-01T00:00'],
        'close_times': ['2021-01-01T01:00'],
        'kms': [0]
    }

    res = insert_to_db(test_dict_single)
    # check for valid insertion
    assert(res.acknowledged)
    assert(db.brevetdb.find_one({'_id': res.inserted_id} is not None))
    # delete from database
    assert(db.brevetdb.find_one_and_delete({'_id': res.inserted_id} is not None))
    assert(db.brevetdb.find_one({'_id': res.inserted_id} is None))
    # try a bigger dictionary
    res = insert_to_db(test_dict_multi)
    # check for valid insertion
    assert(res.acknowledged)
    assert(db.brevetdb.find_one({'_id': res.inserted_id} is not None))
    # delete from database
    assert(db.brevetdb.find_one_and_delete({'_id': res.inserted_id} is not None))
    assert(db.brevetdb.find_one({'_id': res.inserted_id} is None))

def test_db_multi():
    client = MongoClient('mongodb://' + os.environ['MONGODB_HOSTNAME'], 27017)
    db = client.brevetdb

    test_dict_multi = {
        'brev_distance': '1000',
        'open_times': ['2021-01-01T00:00', '2021-01-01T02:56', '2021-01-01T05:53', '2021-01-01T12:08', '2021-01-01T22:22', '2021-01-02T09:05'],
        'close_times': ['2021-01-01T01:00', '2021-01-01T06:40', '2021-01-01T13:30', '2021-01-02T02:40', '2021-01-03T00:45', '2021-01-04T03:00'],
        'kms': ['0', '100', '200', '400', '700', '1000']
    }

    res = insert_to_db(test_dict_multi)
    # check for valid insertion
    assert(res.acknowledged)
    assert(db.brevetdb.find_one({'_id': res.inserted_id} is not None))
    # delete from database
    assert(db.brevetdb.find_one_and_delete({'_id': res.inserted_id} is not None))
    assert(db.brevetdb.find_one({'_id': res.inserted_id} is None))
