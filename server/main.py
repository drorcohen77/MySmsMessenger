from flask import Flask, request, jsonify, Response, request
from flask_cors import CORS
import json
import certifi
from flask_pymongo import PyMongo
import os
from dotenv import load_dotenv
import send_messages
import pymongo


load_dotenv('.env')
app = Flask(__name__)
app.config['MONGO_URI'] = os.environ.get("MONGO_URI")
mongo = PyMongo()
mongo.init_app(app, tlsCAFile=certifi.where())

CORS(app)


### when using comase app locally
# try:
#     mongo = pymongo.MongoClient(
#       host="localhost",
#       port="27017",
#       serverSelectionTimeoutMS=1000
#     )
#     db = mongo.SMSDB
#     mongo.server_info()   # trigger exception if connection to db not succied
# except:
#     print("EROR - Cannot connect to DB")


@app.route('/messages', methods=['GET'])
def get_messages():
    try:
        messages_collection = mongo.db.mySMSmessanger
        messages_list = list(messages_collection.find({}, {"_id": 0}))
    except Exception as ex:
        print(ex)

    return jsonify(messages_list)


@app.route('/add_message', methods=['POST'])
def add_message():
    data = request.json
    destination = destination_fixer(data['phoneNumber'])
    message = data['message']
    send_messages.send_message(destination, message)

    try:
        messages_list = mongo.db.mySMSmessanger
        db_response = messages_list.insert_one(data)
        print(db_response.inserted_id)

        # db_response = db.mySMSmessanger.insert_one(data)  ### when using comase app locally
        # print(db_response.inserted_id)
    except Exception as ex:
        print(ex)

    # return get_messages()
    return Response(
      response=json.dumps({"message": "user created", "id": f'{db_response.inserted_id}'}),
      status=200,
      mimetype="application/json"
    )


def destination_fixer(phone):
    area = '+972'
    destination = "".join([area, phone[1:]])
    return destination


if __name__ == "__main__":
    app.run(debug=True, port=5000)

