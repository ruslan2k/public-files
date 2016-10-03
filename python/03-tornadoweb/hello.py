#!/usr/bin/env python

import base64
import json
import os
import pprint
import re
import sqlite3
import tornado.ioloop
import tornado.web

settings = {
    "node_modules": os.path.join(os.path.dirname(__file__), "node_modules"),
}

DEF_PORT=8888
print(settings)

conn = sqlite3.connect("./db.sq3")
c = conn.cursor()

try:
    c.execute("""CREATE TABLE user (id INTEGER PRIMARY KEY, name TEXT)""")
except sqlite3.OperationalError:
    print("user table already created")

class TableHandler(tornado.web.RequestHandler):
    def get(self, table_name):
        print(table_name)
        tables = c.execute(""" SELECT * FROM sqlite_master WHERE type='table' """)
        q1_columns = """ PRAGMA table_info({0}) """.format(table_name)
        columns = []
        for column in c.execute(q1_columns):
            columns.append({"name": column[1], "type": column[2]})
            print(column)
        pprint.pprint(columns)
        q2_rows = """ SELECT * FROM {0} """.format(table_name)
        print(q2_rows)
        rows = c.execute(q2_rows)
        table_names = [t[1] for t in tables]
        self.render("index.html", rows=rows, tables=table_names)
        # FIXME
        # PRAGMA table_info('user');


class MainHandler(tornado.web.RequestHandler):

    def prepare(self):
        if  "Content-Type" in self.request.headers:
            content_type = self.request.headers["Content-Type"]
            if content_type.startswith("application/json"):
                pprint.pprint(self.request.body)
                self.json_args = tornado.escape.json_decode(self.request.body)
            else:
                self.json_args = None

    #@tornado.web.asynchronous
    def get(self):
        tables = c.execute(""" SELECT * FROM sqlite_master WHERE type='table' """)
        table_names = [t[1] for t in tables]
        if self.get_message():
            message=base64.b64decode(self.get_message())
        else:
            message=None
        self.clear_cookie("message")
        self.render("index.html", tables=table_names)

    def get_message(self):
        message = self.get_cookie("message")
        if message:
            return message
        return None

    def post(self):
        print("POST")
        pprint.pprint(self.json_args)
        table_name = self.get_argument("table_name")
        print(table_name)
        result = re.match(r"^[a-z0-9_]+$", table_name)
        if result:
            q = "CREATE TABLE '{0}' (id INTEGER PRIMARY KEY)".format(table_name)
            print(q)
            c.execute(q)
            self.redirect("/{0}".format(table_name))
        else:
            message = base64.b64encode("Bad table name")
            self.set_cookie("message", message)
            self.redirect("/")
        print(result.groups())
        self.write("POST")

def make_app():
    return tornado.web.Application([
        (r"/(node_modules/angular/angular.js)", tornado.web.StaticFileHandler, {"path": ""}),
        (r"/(node_modules/angular-resource/angular-resource.js)", tornado.web.StaticFileHandler, {"path": ""}),
        (r"/(node_modules/vue/dist/vue.js)", tornado.web.StaticFileHandler, {"path": ""}),
        (r"/(js/app.js)", tornado.web.StaticFileHandler, {"path": ""}),
        (r"/(favicon.ico)", tornado.web.StaticFileHandler, {"path": ""}),
        (r"/", MainHandler),
        (r"/([^/]+)", TableHandler),
    ], debug=True)

if __name__ == "__main__":
    app = make_app()
    print("http://localhost:{0}".format(DEF_PORT))
    app.listen(DEF_PORT)
    tornado.ioloop.IOLoop.current().start()
