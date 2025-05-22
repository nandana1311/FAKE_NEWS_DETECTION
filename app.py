import streamlit as st
import pickle

# Load model
with open("fake_news_model.pkl", "rb") as f:
    model = pickle.load(f)

# UI
st.set_page_config(page_title="Fake News Detector", page_icon="📰")
st.title("📰 Fake News Detection App")
st.markdown("Enter a news article or headline(US political content) to check whether it's **Real** or **Fake**.")

# Input
text_input = st.text_area("Paste News Text Here:", height=200)

# Predict
if st.button("Check News"):
    if text_input.strip() == "":
        st.warning("Please enter some news text first.")
    else:
        prediction = model.predict([text_input])[0]
        if prediction == "FAKE":
            st.error("⚠️ This news appears to be **FAKE**.")
        else:
            st.success("✅ This news appears to be **REAL**.")
