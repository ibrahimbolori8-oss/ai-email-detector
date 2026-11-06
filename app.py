
import streamlit as st
from detector import detect_email

# Page configuration
st.set_page_config(
    page_title="SADIQS AI Email Fraud Detector",
    page_icon="📧",
    layout="centered"
)

# Application title
st.title("📧 SADIQS AI Email Fraud Detector")

st.write(
    "Analyse suspicious emails using machine learning "
    "to identify potential fraud and legitimate messages."
)

st.divider()

# Email input
subject = st.text_input(
    "Email Subject",
    placeholder="Enter email subject..."
)

body = st.text_area(
    "Email Body",
    placeholder="Paste the email content here...",
    height=250
)

# Analyse button
if st.button("🔍 Analyse Email", use_container_width=True):

    if not subject.strip() and not body.strip():

        st.warning("Please enter an email subject or body.")

    else:

        result = detect_email(subject, body)

        fraud_probability = result["fraud_probability"]
        legitimate_probability = result["legitimate_probability"]

        st.divider()

        st.subheader("Analysis Result")

        if result["result"] == "POTENTIAL FRAUD":

            st.error("🚨 POTENTIAL FRAUD")

            st.write(
                "This email has characteristics associated "
                "with fraudulent messages. Do not click "
                "suspicious links or share personal information."
            )

        elif result["result"] == "SUSPICIOUS":

            st.warning("⚠️ SUSPICIOUS EMAIL")

            st.write(
                "This email requires further verification "
                "before taking any action."
            )

        else:

            st.success("✅ LIKELY LEGITIMATE")

            st.write(
                "The model classified this email as likely legitimate. "
                "Still verify the sender before trusting it."
            )

        # Confidence scores
        st.subheader("Detection Confidence")

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "Fraud Score",
                f"{fraud_probability * 100:.2f}%"
            )

        with col2:
            st.metric(
                "Legitimate Score",
                f"{legitimate_probability * 100:.2f}%"
            )

        # Risk bar
        st.subheader("Fraud Risk Level")

        st.progress(fraud_probability)

        st.write(
            f"Estimated fraud score: "
            f"{fraud_probability * 100:.2f}%"
        )

st.divider()

st.caption(
    "SADIQS AI Email Fraud Detector | "
    "Cybersecurity Final Year Project"
)
