import os
import tornado.ioloop
import tornado.web
import sqlite3

settings = {
    "node_modules": os.path.join(os.path.dirname(__file__), "node_modules"),
}

DEF_PORT=8888
print(settings)

conn = sqlite3.connect("./db.sq3")
c = conn.cursor()

try:
    c.execute("""CREATE TABLE user (id INT, name TEXT)""")
except sqlite3.OperationalError:
    print("user table already created")

class TableHandler(tornado.web.RequestHandler):
    def get(self, table_name):
        print(table_name)
        tables = c.execute(""" SELECT * FROM sqlite_master WHERE type='table' """)
        q = """ SELECT * FROM {0} """.format(table_name)
        print(q)
        rows = c.execute(q)
        table_names = [t[1] for t in tables]
        self.render("index.html", rows=rows, tables=table_names)


class MainHandler(tornado.web.RequestHandler):
    #@tornado.web.asynchronous
    def get(self):
        tables = c.execute(""" SELECT * FROM sqlite_master WHERE type='table' """)
        table_names = [t[1] for t in tables]
        self.render("index.html", tables=table_names)

    def post(self):
        self.write("POST")

def make_app():
    return tornado.web.Application([
        (r"/(node_modules/angular/angular.js)", tornado.web.StaticFileHandler, {"path": ""}),
        (r"/(favicon.ico)", tornado.web.StaticFileHandler, {"path": ""}),
        (r"/", MainHandler),
        (r"/([^/]+)", TableHandler),
    ], debug=True)

if __name__ == "__main__":
    app = make_app()
    print("http://localhost:{0}".format(DEF_PORT))
    app.listen(DEF_PORT)
    tornado.ioloop.IOLoop.current().start()
