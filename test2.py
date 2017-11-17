#!/usr/bin/python
# -*- coding: utf-8 -*-
import pymongo
import pymysql

client = pymongo.MongoClient("mongodb://moulick:abc123@localhost")
actor_db = client.sakila
collection = actor_db.actor
print('Connected to MySQL and MongoDB')


conn = pymysql.connect(host='localhost', user='root', password='1011sailboat')

print('Connected to MySQL and MongoDB')

cur = conn.cursor()

cur.execute("SELECT * FROM sakila.actor")
rows = cur.fetchall()


for row in rows:
    data = [('id', row[0]), ('first_name', row[1]), ('last_name', row[2])]
    dicts = dict(data)
    post_id = collection.insert_one(dicts).inserted_id
    print(row[0] ,post_id)
