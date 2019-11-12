
import io
import os

from dotenv import load_dotenv
load_dotenv()

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

def annotate():
    # Instantiates a client
    client = vision.ImageAnnotatorClient()

    # The name of the image file to annotate
    file_name = os.path.abspath('IdDocument-2019-11-12-17.21.png.Png')

    # Loads the image into memory
    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)

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

    annotations = annotate()

    web_entities = get_web_entities(annotations.web_detection)
    if web_entities:
        print('\n{} Web entities found: '.format(
              len(web_entities)))

        for entity in web_entities:
            print('Score      : {}'.format(entity.score))
            print('Description: {}'.format(entity.description))

    text = get_document_text(annotations.full_text_annotation)
    print("\nText found :\n {}".format(text))
