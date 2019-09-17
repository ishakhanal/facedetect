import flask
from flask import request, jsonify
import cv2
import os
import base64

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Face Detection System</h1>
<p>Welcome to ISPAM, we are here to server ai products to you</p>'''

@app.route('/encodeimage', methods=['GET'])
def encodingimage():
	image = open('test1.jpg', 'rb')
	image_read = image.read()
	image_64_encode = base64.urlsafe_b64encode(image_read)

	return image_64_encode

@app.route('/decodeimage', methods=['POST'])
def decodingimage():
	
	data = request.form
	image_64_encode = data['es']


	image_64_decode = base64.urlsafe_b64decode(image_64_encode)
	image_result = open('testimage.jpg', 'wb')
	image_result.write(image_64_decode)
	
	image = cv2.imread('testimage.jpg', 0)

	face_detector = dlib.get_frontal_face_detector()

	img = face_detector(image)

	if img:

		status = "detected"

	else:

		status = "undetected"

	os.remove('testimage.jpg')


	return status


if __name__=='__main__':
	app.run()