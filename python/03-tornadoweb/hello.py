import os
import tornado.ioloop
import tornado.web
import sqlite3

settings = {
    "node_modules": os.path.join(os.path.dirname(__file__), "node_modules"),
}

print(settings)

conn = sqlite3.connect("./db.sq3")
c = conn.cursor()

try:
    c.execute("""CREATE TABLE user (id INT, name TEXT)""")
except sqlite3.OperationalError:
    print("user table already created")

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

class TableHandler(tornado.web.RequestHandler):
    #@tornado.web.asynchronous
    def get(self):
        tables = c.execute(""" SELECT * FROM sqlite_master WHERE type='table' """)
        self.render("index.html", tables=tables)
        #for r in rows:
        #    self.write(dict({"table": r}))

    def post(self):
        self.write("POST")

def make_app():
    return tornado.web.Application([
        (r"/(node_modules/angular/angular.js)", tornado.web.StaticFileHandler, {"path": ""}),
        (r"/(favicon.ico)", tornado.web.StaticFileHandler, {"path": ""}),
        #(r"/_", TableHandler),
        (r"/", TableHandler),
    ], debug=True)

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
