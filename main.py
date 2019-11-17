
import io
import os
import json

from flask import Flask, escape, request, abort, jsonify, send_from_directory
from flask_cors import CORS

from keywords.classification import get_classification

app = Flask(__name__)
CORS(app)

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

from pdf2image import convert_from_bytes, convert_from_path

from dotenv import load_dotenv
load_dotenv()

def pdf_to_image(data):

    first_page = convert_from_bytes(data, 500, single_file=True)[0]
    # first_page = convert_from_path('docs/EmploymentDocument-2019-11-11-09.29.pdf', 500, single_file=True)[0]

    image_data = io.BytesIO()
    first_page.save(image_data, format='PNG')

    image_data.seek(0)
    return image_data.read()

def annotate(image_data):
    # Instantiates a client
    client = vision.ImageAnnotatorClient()

    image = types.Image(content=image_data)

    # Performs label detection on the image file
    response = client.annotate_image({
    'image': image,
    'features': [
            {'type': vision.enums.Feature.Type.TEXT_DETECTION},
            {'type': vision.enums.Feature.Type.WEB_DETECTION}
        ]
    })

    return response


@app.route('/')
def health():
    return jsonify(dict(Health="Alive"))

@app.route("/files", methods=["POST"])
def post_file():
    """Upload a file."""
    file = request.files['file']
    file.seek(0)
    upload_data = file.read()

    # Convert to pdf files to images
    image_data = pdf_to_image(upload_data) if file.filename.lower().endswith('.pdf') else upload_data
    
    annotations = annotate(image_data)
    web_words = [x.description for x in annotations.web_detection.web_entities]
    text_words = annotations.full_text_annotation.text.replace("\n", " ").split()

    return jsonify(dict(Document=get_classification(web_words, text_words)))