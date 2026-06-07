# ---------------- IMPORTS ----------------

import re

# ---------------- CLEAN TEXT FUNCTION ----------------

def clean_text(text):
"""
Cleans and preprocesses the input text.
- Converts text to lowercase
- Removes special characters and numbers
- Splits text into words
"""

```
text = text.lower()

# Remove special characters and numbers
text = re.sub(r'[^a-z\s]', '', text)

# Convert sentence into word list
words = text.split()

return words
```
