import re

# Open and read the text file containing the sample data
# "encoding='utf-8'" ensures proper reading of special characters
with open("sample.txt", "r", encoding="utf-8") as file:
    sample_text = file.read()  # Read the entire content as a single string

# Define regular expression patterns to extract various types of data
patterns = {
    "Emails": r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+",  # Matches emails like user@example.com
    "URLs": r"https?://[^\s]+",  # Matches http and https URLs
    "Phone Numbers": r"\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}",  # Matches various formats of US phone numbers
    "Credit Cards": r"(?:\d{4}[-\s]?){3}\d{4}",  # Matches credit card formats with spaces or hyphens
    "Times": r"\b(?:[01]?\d|2[0-3]):[0-5]\d(?:\s?[APMapm]{2})?\b",  # Matches times like 14:30 or 2:45 PM
    "HTML Tags": r"<[^>]+>",  # Matches any HTML tag like <div>, </a>, etc.
    "Hashtags": r"#\w+",  # Matches hashtags like #regex
    "Currency Amounts": r"\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?"  # Matches currency like $1,000.00
}

# Loop through the patterns and apply each one to the text
for label, regex in patterns.items():
    print(f"\n{label}:")
    matches = re.findall(regex, sample_text)  # Find all matches for this pattern
    if matches:
        for match in matches:
            print(f"  - {match}")
    else:
        print("  - No matches found.")
