from confidence import calculate_confidence_id, calculate_confidence_bank, calculate_confidence_employment

def get_confidences(words):

    scores = dict(id_result = calculate_confidence_id(words),
        bank = calculate_confidence_bank(words),
        employment = calculate_confidence_employment(words))
    valid_scores = dict(filter(lambda x : x[1] != 0, scores.items()))
    return sorted(valid_scores.items(), key=lambda kv: kv[1], reverse=True)


def get_classification(web_words, text_words):

    sorted_x = get_confidences(web_words)

    if (len(sorted_x) == 0):

        web_sorted_x = get_confidences(text_words)
        if (len(web_sorted_x) == 0):
            return ""
        return web_sorted_x[0][0]

    xxx = sorted_x[0]

    if (xxx[1] > 1):
        return xxx[0]

    web_sorted_x = get_confidences(text_words)

    if (len(web_sorted_x) == 0):
        return xxx[0]

    return web_sorted_x[0][0]