class Vision:
    def __init__(self, web_entities, text):
        self.web_entities = web_entities
        self.text = text

class WebEntity:
    def __init__(self, description, score):
        self.description = description
        self.score = score