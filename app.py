from next import hello
from flask import Flask, request, jsonify
import Secrets.Keys
import pymongo
from pymongo import MongoClient
from flask_restful import Api

app = Flask(__name__)

@app.route('/app2/<strx>', methods=['GET'])
def hello_world(strx):
    
    cluster = MongoClient(Secrets.Keys.MongoClientId)
    db = cluster['test']
    collection = db['test']
    post = {"_id": strx, "name": "tushar", "score":5}
    collection.insert_one(post)
    return post

@app.route('/app/next', methods=['GET'])
def returnN():
    return hello()

@app.route('/api', methods=['GET'])
def hello_world1():
    return {"name": "tushar"}

if __name__ == '__main__':
    app.run(debug = True)