from flask import Flask, render_template, redirect, jsonify
from flask_pymongo import PyMongo
import json
from bson.json_util import dumps
from bson.objectid import ObjectId
from flask import request

# Mongo Flask Connection

app = Flask(__name__)


@app.route('/')

def welcome():
    return render_template('landing-page.html')

# Boiler plate 
if __name__ == "__main__":
    app.run(debug=True)
