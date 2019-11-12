import unittest
from confience import calculate_confidence_employment

class TestKeyword(unittest.TestCase):

    def test_1(self):
        input_words = (
            'here is the salary',
            'this is a list of employment docs'
        )
        confdence = calculate_confidence_employment(input_words)
        self.assertEqual(confdence, 2)

if __name__ == '__main__':
    unittest.main()