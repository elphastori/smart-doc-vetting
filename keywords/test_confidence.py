import unittest
from confience import calculate_confidence_employment, calculate_confidence_id

class TestEmploymentKeywords(unittest.TestCase):

    def test_matches(self):
        input_words = (
            'here is the salary',
            'this is a list of employment docs'
        )
        confidence = calculate_confidence_employment(input_words)
        self.assertGreaterEqual(confidence, 0.5)

    def test_no_match(self):
        input_words = (
            'here is the bank statement',
            'this is a list of capitec docs',
            'this is a list of standard bank docs',
        )
        confidence = calculate_confidence_employment(input_words)
        self.assertLessEqual(confidence, 0.5)


class TestIdKeyword(unittest.TestCase):

    def test_matches(self):
        input_words = (
            'rsa id',
            'this from home affairs'
        )
        confidence = calculate_confidence_id(input_words)
        self.assertGreaterEqual(confidence, 0.5)

    def test_no_match(self):
        input_words = (
            'here is the bank statement',
            'this is a list of capitec docs',
            'this is a list of standard bank docs',
        )
        confidence = calculate_confidence_id(input_words)
        self.assertLessEqual(confidence, 0.5)


if __name__ == '__main__':
    unittest.main()