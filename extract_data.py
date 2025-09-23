from regex_patterns import (
    EMAIL_REGEX, URL_REGEX, PHONE_REGEX, CREDIT_CARD_REGEX,
    TIME_REGEX, HTML_TAG_REGEX, HASHTAG_REGEX, CURRENCY_REGEX
)

def extract_data(text):
    results = {
        "emails": EMAIL_REGEX.findall(text),
        "urls": URL_REGEX.findall(text),
        "phones": [int("".join(filter(str.isdigit, match))) for match in PHONE_REGEX.findall(text)],
        "credit_cards": [int("".join(filter(str.isdigit, match))) for match in CREDIT_CARD_REGEX.findall(text)],
        "times": [match[0] + ":" + match[1] if match[1] else match[0] for match in TIME_REGEX.findall(text)],
        "html_tags": HTML_TAG_REGEX.findall(text),
        "hashtags": HASHTAG_REGEX.findall(text),
        "currency": CURRENCY_REGEX.findall(text)
    }
    return results