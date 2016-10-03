#!/usr/bin/env python

import pprint
import sqlite3


conn = sqlite3.connect("./db.sq3")
c = conn.cursor()

try:
    c.execute("""CREATE TABLE user (id INTEGER PRIMARY KEY, name TEXT)""")
except sqlite3.OperationalError:
    print("user table already created")

def getColumns(table_name):
    columns_query = """ PRAGMA table_info({0}) """.format(table_name)
    columns = []
    for column in c.execute(columns_query):
        columns.append({"name": column[1], "type": column[2]})
    return columns
