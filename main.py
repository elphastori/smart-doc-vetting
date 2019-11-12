
import io
import os

from dotenv import load_dotenv
load_dotenv()

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

# Instantiates a client
client = vision.ImageAnnotatorClient()

# The name of the image file to annotate
file_name = os.path.abspath('IdDocument-2019-11-12-17.21.png.Png')

# Loads the image into memory
with io.open(file_name, 'rb') as image_file:
    content = image_file.read()

image = types.Image(content=content)

# Performs label detection on the image file
response = client.label_detection(image=image)
labels = response.label_annotations

print("Smart Document Verification\n")

print('Labels:')
for label in labels:
    print(label.description)