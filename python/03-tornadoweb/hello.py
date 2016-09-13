import tornado.ioloop
import tornado.web
import sqlite3

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
        rows = c.execute(""" SELECT * FROM sqlite_master WHERE type='table' """)
        for r in rows:
            self.write(dict({"table": r}))

def make_app():
    return tornado.web.Application([
        (r"/", TableHandler),
        (r'/(favicon.ico)', tornado.web.StaticFileHandler, {"path": ""}),
    ], debug=True)

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
