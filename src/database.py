# ---------------- IMPORTS ----------------

from pymongo import MongoClient
import tkinter as tk

# ---------------- DATABASE CONNECTION ----------------

client = MongoClient("mongodb://localhost:27017/")

db = client["fake_news_db"]

collection = db["predictions"]

# ---------------- SAVE PREDICTION ----------------

def save_prediction(text, result):

```
data = {
    "text": text,
    "result": result
}

collection.insert_one(data)
```

# ---------------- SHOW STORED DATA ----------------

def show_data():

```
win = tk.Toplevel()

win.title("Stored Predictions")

win.geometry("1000x600")

win.configure(bg="#1e293b")

# Text Area
text_area = tk.Text(
    win,
    bg="#0f172a",
    fg="white",
    font=("Consolas", 11)
)

text_area.pack(fill="both", expand=True)

# Scrollbar
scrollbar = tk.Scrollbar(text_area)

scrollbar.pack(side="right", fill="y")

text_area.config(yscrollcommand=scrollbar.set)

scrollbar.config(command=text_area.yview)

# Display data
for data in collection.find():

    text_area.insert(
        tk.END,
        f"{data['text']}  →  {data['result']}\n\n"
    )
```

# ---------------- CLEAR DATABASE ----------------

def clear_database():

```
collection.delete_many({})
```
