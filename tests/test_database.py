# ---------------- IMPORTS ----------------

from database import (
save_prediction,
clear_database,
collection
)

# ---------------- TEST DATABASE INSERT ----------------

def test_save_prediction():

```
text = "Sample fake news for database testing"

result = "FAKE"

save_prediction(text, result)

data = collection.find_one({"text": text})

assert data is not None

print("Database Insert Test Passed")
```

# ---------------- TEST DATABASE DELETE ----------------

def test_clear_database():

```
clear_database()

count = collection.count_documents({})

assert count == 0

print("Database Clear Test Passed")
```

# ---------------- RUN TESTS ----------------

if **name** == "**main**":

```
test_save_prediction()

test_clear_database()

print("All Database Tests Passed Successfully")
```
