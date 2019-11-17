from confidence import calculate_confidence_id, calculate_confidence_bank, calculate_confidence_employment

def get_confidences(words):

    scores = dict(id_result = calculate_confidence_id(words),
        bank = calculate_confidence_bank(words),
        employment = calculate_confidence_employment(words))
    valid_scores = dict(filter(lambda x : x[1] != 0, scores.items()))
    return sorted(valid_scores.items(), key=lambda kv: kv[1], reverse=True)


def get_classification(web_words, text_words):

    web_class = get_confidences(web_words)

    if (len(web_class) == 0):

        text_class = get_confidences(text_words)
        if (len(text_class) == 0):
            return ""
        return text_class[0][0]

    web_result = web_class[0]

    if (web_result[1] > 1):
        return web_result[0]

    text_class = get_confidences(text_words)

    if (len(text_class) == 0):
        return web_result[0]

    return text_class[0][0]