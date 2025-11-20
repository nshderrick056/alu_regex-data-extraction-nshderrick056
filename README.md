📄 Regex Data Extractor This Python project extracts various data types—such as emails, URLs, phone numbers, credit card numbers, times, HTML tags, hashtags, and currency amounts—from a given text file using regular expressions.

🚀 Project Overview Regular expressions (regex) are powerful tools for pattern matching in text. This project demonstrates how to use them in Python to scan a text file and extract useful information automatically.

📂 Project Structure bash Copy Edit alu_regex-data-extraction-nshderrick056/ │ ├── regex_extractor.py # Main Python script with regex patterns and extraction logic ├── sample.txt # Sample text file containing raw data to be processed └── README.md # This file 📌 Features ✅ Extracts common patterns from unstructured text

✉️ Emails

🌐 URLs

📞 Phone Numbers

💳 Credit Card Numbers

⏰ Times (e.g., 14:45 or 2:30 PM)

🏷 HTML Tags

🧵 Hashtags

💰 Currency Amounts

📥 How to Use Clone the repository (or download the folder):

bash Copy Edit 
git clone https://github.com/nshderrick056/alu_regex-data-extraction-nshderrick056.git 
cd alu_regex-data-extraction-nshderrick056 Add your sample text to the sample.txt file.

Make sure it's in the same directory as regex_extractor.py.

Run the script using Python:

bash Copy Edit python regex_extractor.py 🧠 How It Works The script opens and reads the contents of sample.txt using utf-8 encoding.

It then applies multiple regular expression patterns to extract relevant information.

Each type of data is printed to the terminal in a categorized format.

💡 Sample Output markdown Copy Edit Emails:

user@example.com
URLs:

https://example.org
Phone Numbers:

(123) 456-7890
Credit Cards:

1234-5678-9012-3456
Times:

14:30
2:45 PM
HTML Tags:

Hashtags:

#regex
#python
Currency Amounts:

$1,200.00
