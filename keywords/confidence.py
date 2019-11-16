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
    'earnings']

# _BANK_EXHAUSTIVE_KEYWORDS = [
#     'Received',
#     'Verify',
#     'Statement',
#     'reference',
#     'Refunds',
#     'Adjustments',
#     'Transfers',
#     'Number',
#     'Inter-Account',
#     'FNB',
#     'Overdraft',
#     'Dr',
#     'Deposits',
#     'Cr',
#     'Overdraft',
#     'Payments',
#     'Withdrawals',
#     'Interest',
#     'Fees',
#     'F.N.B.',
#     'Corporation'
# ]

_BANK_KEYWORDS = [
    'bank'
]

_ID_KEYWORDS = [
    'rsa',
    'country',
    'id',
    'home affairs']

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
        if ratio > 50:
            final_ratio += 1
    return final_ratio