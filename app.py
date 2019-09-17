import flask
import cv2
import dlib
import os
import base64
from flask import request, jsonify


app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Face Detection System</h1>
<p>Welcome to ISPAM, we are here to server ai products to you</p>'''

if __name__=='__main__':
	app.run()