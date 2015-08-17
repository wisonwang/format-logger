#!/usr/bin/env python
# -*- coding: utf-8; mode: python; tab-width: 4; indent-tabs-mode: nil; c-basic-offset: 4 -*- vim:fenc=utf-8:ft=python:et:sw=4:ts=4:sts=4

import getopt, sys
import logging

import pymongo

def test_mongo_client():
    client = pymongo.MongoClient()
    db = client.test
    db.drop_collection("test")
    db.create_collection("test")
    collection = db.get_collection("test")
    student = dict()
    student['name'] = 'hello kitty'
    student['agge'] = 12
    student['id'] = '20150813'
    collection.insert(student)
    records = collection.find({'id':'20150813'})
    for r in records:
        if r['id'] == 12:
            print 'find zhe record ok'
            return
    db.drop_collection("test")
    raise 'error happended'

class Format_Logger_Handler(object):
    