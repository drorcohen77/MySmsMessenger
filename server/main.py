from flask import Flask, request, jsonify, Response
from flask_cors import CORS
from flask_pymongo import PyMongo
import send_messages
import certifi

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb+srv://dror:Almog20haifa!@cluster0.vk6vnph.mongodb.net/SMSDB?retryWrites=true&w=majority'
mongo = PyMongo()

CORS(app)
mongo.init_app(app, tlsCAFile=certifi.where())


messages = [
  {'id': 1, 'phoneNumber': '888-999-999', 'message': 'hello', 'time': '01/01/2020', 'charNum': '20/100'},
  {'id': 2, 'phoneNumber': '111-888-999', 'message': 'world', 'time': '04/04/2020', 'charNum': '90/100'},
  {'id': 3, 'phoneNumber': '222-333-666', 'message': 'python', 'time': '05/05/2020', 'charNum': '50/100'},
]


@app.route('/messages', methods=['GET'])
def get_messages():
    messages_collection = mongo.db.mySMSmessanger
    messages_list = list(messages_collection.find({}, {"_id": 0}))
    return jsonify(messages_list)


@app.route('/add_message', methods=['POST'])
def add_message():
    data = request.json
    destination = destination_fixer(data['phoneNumber'])
    message = data['message']
    send_messages.send_message(destination, message)

    messages_list = mongo.db.mySMSmessanger
    messages_list.insert_one(data)
    return get_messages()


def destination_fixer(phone):
    area = '+972'
    destination = "".join([area, phone[1:]])
    return destination


app.run(debug=True, port=5000)

