from models import Vision
from models import WebEntity

import operator

from data_id import id_result
from data_bank import bank
from data_employment import employment

import unittest
from confidence import calculate_confidence_id, calculate_confidence_bank, calculate_confidence_employment
from classification import get_classification

class TestIdKeyword(unittest.TestCase):

    def test_matches(self):

        expected = "id_result"

        id_words = [web_entity.description for web_entity in id_result.web_entities]

        doc_type = get_classification(id_words)

        self.assertEqual(expected, doc_type)

class TestBankKeyword(unittest.TestCase):

    def test_matches(self):

        expected = "bank"

        bank_words = [web_entity.description for web_entity in bank.web_entities]

        doc_type = get_classification(bank_words)

        self.assertEqual(expected, doc_type)

class TestEmploymentKeyword(unittest.TestCase):

    def test_matches(self):

        expected = "employment"

        employment_words = [web_entity.description for web_entity in employment.web_entities]

        doc_type = get_classification(employment_words)

        self.assertEqual(expected, doc_type)

if __name__ == '__main__':
    unittest.main()