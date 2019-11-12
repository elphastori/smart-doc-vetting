import unittest
from confience import calculate_confidence_employment

class TestKeyword(unittest.TestCase):

    def test_1(self):
        input_words = (
            'here is the salary',
            'this is a list of employment docs'
        )
        confidence = calculate_confidence_employment(input_words)
        self.assertGreaterEqual(confidence, 0.5)

    def test_2(self):
        input_words = (
            'here is the bank statement',
            'this is a list of capitec docs',
            'this is a list of standard bank docs',
        )
        confidence = calculate_confidence_employment(input_words)
        self.assertLessEqual(confidence, 0.5)

if __name__ == '__main__':
    unittest.main()