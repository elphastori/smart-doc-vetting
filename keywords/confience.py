from fuzzywuzzy import fuzz
from fuzzywuzzy import process

space = ' '
employment_keywords = [
    'salary',
    'advice',
    'payslip',
    'pay',
    'slip',
    'employment',
    'hours',
    'employee',
    'earnings']
    
def calculate_confidence_employment(input_list : list):
    words = space.join(input_list)
    final_ratio = 0
    for keyword in employment_keywords:
        ratio = fuzz.partial_ratio(words, keyword)
        if ratio > 50:
            final_ratio += 1
    return final_ratio