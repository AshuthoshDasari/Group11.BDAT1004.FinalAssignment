#importing libraries
from flask import Flask, render_template, request, jsonify
import json
import requests
import certifi
from pymongo import MongoClient
import time
import schedule


client = MongoClient("mongodb+srv://ashuthosh:test@ashuthoshcluster.wzfht.mongodb.net", tlsCAFile=certifi.where())
db = client.get_database('db')
records = db.data



def put_data(db):
        
    while True:
        r = requests.get('https://api.covid19api.com/summary')
        if r.status_code == 200:
            data = r.json()
            # print(data)
            db.data.insert_one(data)
            time.sleep(10)
    else:
        exit()


schedule.every(2).seconds.do(put_data(db))




# while True:
#     r = requests.get('https://api.covid19api.com/summary')
#     if r.status_code == 200:
#         data = r.json()
#         # print(data)
#         db.data.insert_one(data)
#         time.sleep(60)
# else:
#     exit()

# records.count_documents({})
