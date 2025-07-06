import re

# Utility function to tokenize text into words
# This function uses a regular expression to find all words in the text,
def tokenize(text):
    return re.findall(r'\b\w+\b', text.lower())
