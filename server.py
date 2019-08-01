# -*- coding: utf-8 -*-
from http.server import BaseHTTPRequestHandler,HTTPServer
import sqlite3
import random

conn = sqlite3.connect("hostbase.db")  # или :memory: чтобы сохранить в RAM
cursor = conn.cursor()
cursor.execute("CREATE TABLE if not exists users_remote (host text, id text, time text, user text, password text)")

def sql_add(host='', id='', time='', user='', password=''):
    sql = 'INSERT INTO users_remote VALUES ("'+host+'","'+id+'","'+time+'","'+user+'","'+password+'")'
    cursor.execute(sql)
    conn.commit()
    return

def sql_qeury(self):
    cursor.execute(self)
    qeury = str(cursor.fetchall())[3:-4]
    return qeury

cursor.execute("""SELECT * FROM users_remote""")
print(cursor.fetchall())

class GetHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        qeury = self.path[1:].encode()
        qeury_dict={}
        for i in qeury.decode().split('&'):
            y =i.split('=')
            qeury_dict[y[0]]=y[1]

        if 'host' in qeury_dict:
            qeury = sql_qeury('SELECT id FROM users_remote WHERE host="' + qeury_dict['host'] + '"')
            if qeury == '':
                add_id = str(random.randint(100000000,999999999))
                sql_add(host=qeury_dict['host'],id=add_id)
                qeury = add_id
            self.wfile.write(qeury.encode())
        elif 'id' in qeury_dict:
            qeury = sql_qeury('SELECT host FROM users_remote WHERE id="' + qeury_dict['id'] + '"')
            if qeury == '':
                qeury = 'Bad id = ' + qeury_dict['id']
            self.wfile.write(qeury.encode())
        else:
            self.wfile.write('Bad Get'.encode())
        return


if __name__ == '__main__':

    server = HTTPServer(('0.0.0.0', 19191), GetHandler)
    server.serve_forever()