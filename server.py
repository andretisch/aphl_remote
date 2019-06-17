# -*- coding: utf-8 -*-
from BaseHTTPServer import BaseHTTPRequestHandler
from BaseHTTPServer import HTTPServer
import os

import sqlite3
conn = sqlite3.connect("mydatabase.db") # или :memory: чтобы сохранить в RAM
cursor = conn.cursor()

if os.path.exists("mydatabase.db") == False:
    cursor.execute("""CREATE TABLE albums(title text, artist text, release_date text,publisher text, media_type text)""")

class GetHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        qeury = self.path[1:]
        print qeury
        self.wfile.write(qeury)
        return


if __name__ == '__main__':

    server = HTTPServer(('0.0.0.0', 19191), GetHandler)
    server.serve_forever()