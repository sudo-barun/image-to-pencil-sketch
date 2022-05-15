import os
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import random
import string
from SketchConverter import SketchConverter
import cv2
import base64

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def form():
	if request.method == 'POST':
		return submit_form()
	else:
		return show_form()


def show_form():
	return render_template('form.html')


def submit_form():
	uploaded_image = request.files['image']
	upload_path = get_upload_file_path(uploaded_image.filename)
	uploaded_image.save(upload_path)

	converter = SketchConverter(upload_path)
	converter.convert()
	sketch_path = '-converted'.join(os.path.splitext(upload_path))
	cv2.imwrite(sketch_path, converter.sketch)

	view_vars = {
		"image_base64": image_to_base64(upload_path),
		"sketch_base64": image_to_base64(sketch_path),
	}

	return render_template('result.html', **view_vars)


def image_to_base64(image_path):
	with open(image_path, 'rb') as image_file:
		return 'data:image/png;base64,'+base64.b64encode(image_file.read()).decode()


def get_project_path():
	return os.path.dirname(os.path.abspath(__file__))


def get_upload_path():
	return get_project_path()+'/uploads'


def get_upload_file_path(filename):
	filename = secure_filename(filename)
	suffix = '-'+''.join(random.choice(string.ascii_letters) for _ in range(5))
	filename = suffix.join(os.path.splitext(filename))
	return get_upload_path()+'/'+filename
