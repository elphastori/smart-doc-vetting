class Vision:
    def __init__(self, web_entities, text):
        self.web_entities = web_entities
        self.text = text

    def serialize(self):
        return dict(web_entities = [web_entity.serialize() for web_entity in self.web_entities], text = self.text)

class WebEntity:
    def __init__(self, description, score):
        self.description = description
        self.score = score

    def serialize(self):
        return dict(description = self.description, score = self.score)