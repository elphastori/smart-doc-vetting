from confidence import calculate_confidence_id, calculate_confidence_bank, calculate_confidence_employment

def get_classification(words):

    id_confidence = calculate_confidence_id(words)

    bank_confidence = calculate_confidence_bank(words)

    employment_confidence = calculate_confidence_employment(words)

    scores = dict(id = id_confidence, bank = bank_confidence, employment = employment_confidence)

    valid_scores = dict(filter(lambda x : x[1] != 0, scores.items()))

    sorted_x = sorted(valid_scores.items(), key=lambda kv: kv[1], reverse=True)

    first = sorted_x[0][0]
    # second = sorted_x[0][0]

    return first