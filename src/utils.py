# ---------------- IMPORTS ----------------

from tkinter import messagebox

# ---------------- SHOW SUCCESS MESSAGE ----------------

def show_success(title, message):

```
messagebox.showinfo(title, message)
```

# ---------------- SHOW ERROR MESSAGE ----------------

def show_error(title, message):

```
messagebox.showerror(title, message)
```

# ---------------- SHOW WARNING MESSAGE ----------------

def show_warning(title, message):

```
messagebox.showwarning(title, message)
```

# ---------------- FORMAT PERCENTAGE ----------------

def format_percentage(value):

```
return f"{value:.2f}%"
```

# ---------------- VALIDATE INPUT ----------------

def validate_input(text):

```
if text.strip() == "":
    return False

return True
```
