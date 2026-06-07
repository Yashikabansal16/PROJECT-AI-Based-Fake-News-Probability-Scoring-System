# ---------------- IMPORTS ----------------

import tkinter as tk
from tkinter import messagebox

from preprocessing import clean_text
from predictor import load_dataset, predict_news
from visualization import show_graph
from database import show_data, clear_database

# ---------------- GLOBAL SESSION ----------------

session_data = []

# ---------------- BUTTON FUNCTIONS ----------------

def analyze_news():
text = entry.get("1.0", tk.END).strip()

```
if text == "":
    messagebox.showwarning("Warning", "Enter news text")
    return

result, confidence, color = predict_news(text)

session_data.append(result)

result_label.config(
    text=f"Result: {result} ({confidence:.2f}%)",
    fg=color
)
```

def clear_input():
entry.delete("1.0", tk.END)
result_label.config(text="")

def clear_graph():
global session_data
session_data = []
messagebox.showinfo("Cleared", "Graph data cleared")

# ---------------- UI ----------------

root = tk.Tk()
root.title("AI Based Fake News Probability Scoring System")
root.state("zoomed")
root.configure(bg="#0f172a")

main_frame = tk.Frame(root, bg="#0f172a")
main_frame.pack(expand=True)

# ---------------- TITLE ----------------

title = tk.Label(
main_frame,
text="📰 Fake News Detection System",
font=("Segoe UI", 26, "bold"),
fg="white",
bg="#0f172a"
)
title.pack(pady=15)

# ---------------- LOAD DATASET ----------------

tk.Button(
main_frame,
text="📂 Load Dataset",
command=load_dataset,
bg="#14b8a6",
fg="white",
font=("Segoe UI", 12, "bold"),
width=22,
height=2
).pack(pady=10)

# ---------------- TEXT INPUT ----------------

entry = tk.Text(
main_frame,
height=5,
width=70,
font=("Segoe UI", 12),
bg="#1e293b",
fg="white",
insertbackground="white"
)
entry.pack(pady=10)

# ---------------- ANALYZE BUTTON ----------------

tk.Button(
main_frame,
text="🔍 Analyze News",
command=analyze_news,
bg="#3b82f6",
fg="white",
font=("Segoe UI", 13, "bold"),
width=20
).pack(pady=10)

# ---------------- RESULT LABEL ----------------

result_label = tk.Label(
main_frame,
text="",
font=("Segoe UI", 16, "bold"),
bg="#0f172a"
)
result_label.pack(pady=8)

# ---------------- BUTTON FRAME ----------------

btn_frame = tk.Frame(main_frame, bg="#0f172a")
btn_frame.pack(pady=15)

btn_style = {
"width": 20,
"height": 2,
"font": ("Segoe UI", 11, "bold")
}

# ---------------- EXTRA BUTTONS ----------------

tk.Button(
btn_frame,
text="📊 Graph",
bg="#f59e0b",
fg="white",
command=lambda: show_graph(session_data),
**btn_style
).grid(row=0, column=0, padx=10, pady=10)

tk.Button(
btn_frame,
text="📂 Data",
bg="#10b981",
fg="white",
command=show_data,
**btn_style
).grid(row=0, column=1, padx=10, pady=10)

tk.Button(
btn_frame,
text="🧹 Clear Input",
bg="#6366f1",
fg="white",
command=clear_input,
**btn_style
).grid(row=1, column=0, padx=10, pady=10)

tk.Button(
btn_frame,
text="🗑 Clear Graph",
bg="#eab308",
fg="black",
command=clear_graph,
**btn_style
).grid(row=1, column=1, padx=10, pady=10)

tk.Button(
btn_frame,
text="🗑 Clear Database",
bg="#ef4444",
fg="white",
command=clear_database,
**btn_style
).grid(row=2, column=0, padx=10, pady=10)

# ---------------- RUN APP ----------------

root.mainloop()

