from models import Vision
from models import WebEntity

from data_bank import bank

import unittest
from confidence import calculate_confidence_id, calculate_confidence_bank, calculate_confidence_employment

class TestBankKeyword(unittest.TestCase):

    def test_matches(self):

        expected = 

        id_words = [web_entity.description for web_entity in bank.web_entities]
        id_confidence = calculate_confidence_id(id_words)

        bank_words = [web_entity.description for web_entity in bank.web_entities]
        bank_confidence = calculate_confidence_bank(bank_words)

        employment_words = [web_entity.description for web_entity in bank.web_entities]
        employment_confidence = calculate_confidence_employment(employment_words)

        scores = dict(id = id_confidence, bank = bank_confidence, employment = employment_confidence)

        valid_scores = score for score in 

        self.assertGreaterEqual(confidence, 0.5)

if __name__ == '__main__':
    unittest.main()