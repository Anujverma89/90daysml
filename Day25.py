import streamlit as st
from textblob import TextBlob

def get_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    if polarity > 0.1:
        return "Positive:)"
    elif polarity < -0.1:
        return "Negative:("
    else:
        return "Neutral --"

# Streamlit UI
st.set_page_config(page_title="Day 25 - Sentiment Analyzer", layout="centered")

st.title("📘 Day 25: Sentiment Analyzer")
st.write("Enter some text below and get the sentiment (Positive, Neutral, or Negative).")

user_input = st.text_area("Your Text", height=150)

if st.button("Analyze Sentiment"):
    if user_input.strip() == "":
        st.warning("Please enter some text.")
    else:
        sentiment = get_sentiment(user_input)
        st.success(f"Sentiment: **{sentiment}**")
