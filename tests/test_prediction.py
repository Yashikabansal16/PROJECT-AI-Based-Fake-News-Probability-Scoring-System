# ---------------- IMPORTS ----------------

from predictor import predict_news

# ---------------- TEST FAKE NEWS ----------------

def test_fake_news():

```
text = "Breaking shocking secret government conspiracy exposed"

result, confidence, color = predict_news(text)

assert result in ["FAKE", "REAL"]

print("Fake News Test Passed")
```

# ---------------- TEST REAL NEWS ----------------

def test_real_news():

```
text = "The government announced new education policies today"

result, confidence, color = predict_news(text)

assert result in ["FAKE", "REAL"]

print("Real News Test Passed")
```

# ---------------- RUN TESTS ----------------

if **name** == "**main**":

```
test_fake_news()

test_real_news()

print("All Prediction Tests Passed Successfully")
```
