# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

def annotate_pdf(file_name):
    # Instantiates a client
    client = vision.ImageAnnotatorClient()
    #feature = vision.types.Feature(type=vision.enums.Feature.Type.DOCUMENT_TEXT_DETECTION)
    # https://cloud.google.com/vision/docs/pdf#vision_text_detection_pdf_gcs-python
    image = types.Image(content="get_image(file_name)")

    # Performs label detection on the image file
    response = client.annotate_image({
    'image': image,
    'features': [
            {'type': vision.enums.Feature.Type.TEXT_DETECTION},
            {'type': vision.enums.Feature.Type.WEB_DETECTION}
        ]
    })

    return response