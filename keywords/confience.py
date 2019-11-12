employment_keywords = (
    'salary',
    'advice',
    'payslip',
    'pay',
    'slip',
    'employment',
    'hours',
    'employee',
    'earnings')
    
def calculate_confidence_employment(input_list : list):
    words = [paragraph.split() for paragraph in input_list]
    return len(words)