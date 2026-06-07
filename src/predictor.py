# ---------------- IMPORTS ----------------

import math
import pandas as pd
from collections import defaultdict
from tkinter import filedialog, messagebox

from preprocessing import clean_text
from database import save_prediction

# ---------------- GLOBAL VARIABLES ----------------

fake_words = defaultdict(int)
real_words = defaultdict(int)

fake_total = 0
real_total = 0
V = 0

# ---------------- LOAD DATASET ----------------

def load_dataset():
global fake_words, real_words
global fake_total, real_total, V

```
file_path = filedialog.askopenfilename(
    filetypes=[
        ("CSV files", "*.csv"),
        ("Excel files", "*.xlsx")
    ]
)

if not file_path:
    return

try:
    # Read dataset
    if file_path.endswith(".csv"):
        df = pd.read_csv(file_path)
    else:
        df = pd.read_excel(file_path)

    # Clear old data
    fake_words.clear()
    real_words.clear()

    fake_total = 0
    real_total = 0

    # Train model
    for _, row in df.iterrows():

        words = clean_text(str(row['text']))

        if row['label'] == "FAKE":

            for word in words:
                fake_words[word] += 1
                fake_total += 1

        else:

            for word in words:
                real_words[word] += 1
                real_total += 1

    # Vocabulary size
    V = len(set(
        list(fake_words.keys()) +
        list(real_words.keys())
    ))

    messagebox.showinfo(
        "Dataset Loaded",
        f"Dataset loaded successfully!\nRows: {len(df)}"
    )

except Exception as e:
    messagebox.showerror("Error", str(e))
```

# ---------------- PREDICT NEWS ----------------

def predict_news(text):
global fake_total, real_total, V

```
words = clean_text(text)

# Initial probabilities
log_fake = math.log(fake_total / (fake_total + real_total))
log_real = math.log(real_total / (fake_total + real_total))

# Naive Bayes probability calculation
for word in words:

    log_fake += math.log(
        (fake_words[word] + 1) /
        (fake_total + V)
    )

    log_real += math.log(
        (real_words[word] + 1) /
        (real_total + V)
    )

# Prevent overflow
max_log = max(log_fake, log_real)

fake_prob = math.exp(log_fake - max_log)
real_prob = math.exp(log_real - max_log)

total = fake_prob + real_prob

fake_percent = (fake_prob / total) * 100
real_percent = (real_prob / total) * 100

# Final prediction
if fake_percent > real_percent:
    result = "FAKE"
    confidence = fake_percent
    color = "#ef4444"

else:
    result = "REAL"
    confidence = real_percent
    color = "#22c55e"

# Save to database
save_prediction(text, result)

return result, confidence, color
```
