from flask import Flask, request, jsonify
import Secrets.Keys
import pymongo
from pymongo import MongoClient

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def hello_world():
    MongoClientId = Secrets.Keys.MongoClientId
    cluster = MongoClient(MongoClientId)
    db = cluster['test']
    collection = db['test']
    post = {"_id": str(request.args['Query']), "name": "tushar", "score":5}
    collection.insert_one(post)
    return post

if __name__ == '__main__':
    app.run()
                      
