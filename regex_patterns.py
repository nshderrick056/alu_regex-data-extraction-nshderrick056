import re

# Email regex
EMAIL_REGEX = re.compile(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}')

# URL regex (allowing "Links to an external site." to be ignored if present)
URL_REGEX = re.compile(r'https?://[a-zA-Z0-9.-]+(?:/[^\s]*)?')

# Phone regex (various formats)
PHONE_REGEX = re.compile(r'(?:\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4})')

# Credit card regex (with spaces or dashes)
CREDIT_CARD_REGEX = re.compile(r'(?:\d{4}[- ]?){3}\d{4}')

# Time regex (12-hour and 24-hour)
TIME_REGEX = re.compile(
    r'^(?:([01]?\d|2[0-3]):([0-5]\d)(?:\s?(?:AM|PM|am|pm))?)$'
)

# HTML tags regex
HTML_TAG_REGEX = re.compile(r'<[^>]+>')

# Hashtag regex
HASHTAG_REGEX = re.compile(r'#\w+')

# Currency regex
CURRENCY_REGEX = re.compile(r'\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?')