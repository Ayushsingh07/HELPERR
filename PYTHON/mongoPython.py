# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 18:10:23 2022

@author: INAKKAM
"""

from pymongo import MongoClient

def mongoConnect():
    client = MongoClient();
    print("Connection Successful")
    client.close()

mongoConnect()
print("fwdf")
