from flask import Flask, request, jsonify
import pymongo
from pymongo import MongoClient

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def hello_world():
    
    cluster = MongoClient("mongodb+srv://Algoristy:Algoristy@fakenewsdetector.gv1x5.mongodb.net/test?retryWrites=true&w=majority")
    db = cluster['test']
    collection = db['test']
    post = {"_id": str(request.args['Query']), "name": "tushar", "score":5}
    collection.insert_one(post)
    d = {}
    d['Query'] = str(request.args['Query'])
    return jsonify(d)

if __name__ == '__main__':
    app.run()
                      
