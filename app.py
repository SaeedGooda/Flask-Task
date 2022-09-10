import flask
from flask import request, jsonify
import pymongo

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Initialize the mongodb variables
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["user"]

# endpoint that takes {"username": "Saeed", "password": "123456", "age": "22"}
@app.route('/createUser', methods=['Post'])
def create():
    data = request.get_json()
    x = mycol.insert_one(data)
    print(x)

if __name__ == "__main__":
    app.run()