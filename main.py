
import io
import os

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

from pdf2image import convert_from_path

from dotenv import load_dotenv
load_dotenv()

def get_image(file_name):
    file_path = os.path.abspath(file_name)

    if not file_name.lower().endswith('.pdf'):
        # Loads the image into memory
        with io.open(file_path, 'rb') as image_file:
            return image_file.read()
    
    # convert pdf to image
    first_page = convert_from_path(file_path, 500, single_file=True)[0]

    image_data = io.BytesIO()
    first_page.save(image_data, format='PNG')

    image_data.seek(0)
    return image_data.read()

def annotate_pdf(file_name):
    # Instantiates a client
    client = vision.ImageAnnotatorClient()
    feature = vision.types.Feature(type=vision.enums.Feature.Type.DOCUMENT_TEXT_DETECTION)
    # https://cloud.google.com/vision/docs/pdf#vision_text_detection_pdf_gcs-python
    image = types.Image(content=get_image(file_name))

    # Performs label detection on the image file
    response = client.annotate_image({
    'image': image,
    'features': [
        {'type': vision.enums.Feature.Type.TEXT_DETECTION},
        {'type': vision.enums.Feature.Type.WEB_DETECTION}
        ],
    })

    return response

def annotate(file_name):
    # Instantiates a client
    client = vision.ImageAnnotatorClient()

    image = types.Image(content=get_image(file_name))

    # Performs label detection on the image file
    response = client.annotate_image({
    'image': image,
    'features': [
        {'type': vision.enums.Feature.Type.TEXT_DETECTION},
        {'type': vision.enums.Feature.Type.WEB_DETECTION}
        ],
    })

    return response


def get_web_entities(annotations):
    """Returns detected features in the provided web annotations."""
    return annotations.web_entities


def get_document_text(annotations):
    return annotations.text


if __name__ == '__main__':
    print("Smart Document Verification\n")

    annotations = annotate('BankStatement-2019-11-11-09.28.pdf')

    web_entities = get_web_entities(annotations.web_detection)
    if web_entities:
        print('\n{} Web entities found: '.format(
              len(web_entities)))

        for entity in web_entities:
            print('Score      : {}'.format(entity.score))
            print('Description: {}'.format(entity.description))

    text = get_document_text(annotations.full_text_annotation)
    print("\nText found :\n {}".format(text))
