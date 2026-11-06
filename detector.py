
import joblib
import os

# Model location
MODEL_PATH = "model.pkl"

# Check whether the trained model exists
if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(
        "Model not found. Please run train_model.py first."
    )

# Load trained machine learning pipeline
model = joblib.load(MODEL_PATH)


def detect_email(subject, body):

    # Combine subject and email body
    email_text = str(subject) + " " + str(body)

    if not email_text.strip():
        raise ValueError("Please provide an email subject or body.")

    # Predict email category
    prediction = model.predict([email_text])[0]

    # Get prediction probabilities
    probabilities = model.predict_proba([email_text])[0]

    # Match probabilities to their respective labels
    class_probabilities = dict(
        zip(model.classes_, probabilities)
    )

    fraud_probability = float(
        class_probabilities.get("fraud", 0)
    )

    legitimate_probability = float(
        class_probabilities.get("legitimate", 0)
    )

    # Determine risk classification
    if fraud_probability >= 0.70:
        result = "POTENTIAL FRAUD"

    elif fraud_probability >= 0.40:
        result = "SUSPICIOUS"

    else:
        result = "LIKELY LEGITIMATE"

    return {
        "result": result,
        "fraud_probability": fraud_probability,
        "legitimate_probability": legitimate_probability
    }
