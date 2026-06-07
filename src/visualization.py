# ---------------- IMPORTS ----------------

import matplotlib.pyplot as plt
from tkinter import messagebox

# ---------------- SHOW GRAPH ----------------

def show_graph(session_data):

```
fake_count = session_data.count("FAKE")

real_count = session_data.count("REAL")

total = fake_count + real_count

if total == 0:

    messagebox.showwarning(
        "No Data",
        "No predictions available!"
    )

    return

# ---------------- GRAPH WINDOW ----------------
plt.figure(figsize=(8, 5))

bars = plt.bar(
    ["FAKE", "REAL"],
    [fake_count, real_count],
    color=["#ef4444", "#22c55e"],
    width=0.5
)

# ---------------- TITLE ----------------
plt.title(
    "Prediction Distribution",
    fontsize=14,
    fontweight="bold"
)

plt.ylabel("Number of Predictions")

# ---------------- VALUES ON BARS ----------------
for bar in bars:

    height = bar.get_height()

    plt.text(
        bar.get_x() + bar.get_width()/2,
        height + 0.1,
        f"{int(height)}",
        ha="center",
        va="bottom",
        fontsize=11,
        fontweight="bold"
    )

# ---------------- STYLING ----------------
plt.ylim(0, max(fake_count, real_count) + 2)

plt.grid(
    axis="y",
    linestyle="--",
    alpha=0.3
)

# ---------------- WINDOW POSITION ----------------
manager = plt.get_current_fig_manager()

try:
    manager.window.wm_geometry("+300+120")

except:
    pass

plt.tight_layout()

plt.show()
```
