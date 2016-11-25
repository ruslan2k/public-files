#!/usr/bin/env python

import pprint
import sqlite3


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


conn = sqlite3.connect("./db.sq3")
#conn.row_factory = dict_factory
c = conn.cursor()


def listOfBin2Str(l_bin, encoding="utf-8"):
    ret = list(map(lambda b: b.decode(encoding), l_bin))[0]
    return ret

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

def getRows(table_name):
    rows_query = """SELECT * FROM {0}""".format(table_name)
    rows = []
    columns = getColumns(table_name)
    for row in c.execute(rows_query):
        row_d = {}
        i = 0
        for col in columns:
            row_d[col["name"]] = row[i]
            i += 1
        rows.append(row_d)
    return rows


def save(table_name, data_dict):
    cols = ",".join(data_dict.keys())
    vals = ",".join(map(lambda v: "'{0}'".format(listOfBin2Str(v)), data_dict.values()))
    pprint.pprint(cols)
    pprint.pprint(vals)
    sql = "INSERT INTO '{0}' ({1}) VALUES ({2})".format(table_name, cols, vals)
    pprint.pprint(sql)
    c.execute(sql)
