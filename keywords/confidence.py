from fuzzywuzzy import fuzz
from fuzzywuzzy import process

space = ' '

_EMPLOYMENT_KEYWORDS = [
    'salary',
    'advice',
    'payslip',
    'pay',
    'slip',
    'employment',
    'hours',
    'employee',
    'earnings',
    'resources'
]

_BANK_KEYWORDS = [
    'bank',
    'Received',
    'Statement',
    'reference',
    'Refunds',
    'Adjustments',
    'Transfers',
    'Inter-Account',
    'FNB',
    'Overdraft',
    'Dr',
    'Deposits',
    'Cr',
    'Overdraft',
    'Payments',
    'Withdrawals',
    'Interest',
    'Fees',
    'F.N.B.',
    'Corporation'
]

_ID_KEYWORDS = [
    'rsa',
    'country',
    'id',
    'identity',
    'home affairs'
]

_RESIDENCE_KEYWORDS = [
]

def calculate_confidence_employment(input_list : list):
    return _calc_confidence(_EMPLOYMENT_KEYWORDS, input_list)

def calculate_confidence_bank(input_list : list):
    return _calc_confidence(_BANK_KEYWORDS, input_list)

def calculate_confidence_id(input_list : list):
    return _calc_confidence(_ID_KEYWORDS, input_list)

def _calc_confidence(key_words_list : list, input_list: list):
    words = space.join(input_list)
    final_ratio = 0
    for keyword in key_words_list:
        ratio = fuzz.partial_ratio(words, keyword)
        if ratio > 75:
            final_ratio += 1
    return final_ratio