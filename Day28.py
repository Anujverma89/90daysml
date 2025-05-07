import streamlit as st
import pandas as pd

# Load dataset
@st.cache_data
def load_data():
    return pd.read_csv("prescription_prices.csv")

df = load_data()

st.title("💊 Prescription Price Checker")
st.subheader("Find cheaper, generic alternatives to expensive medicines")

# Search box
query = st.text_input("Enter the brand or generic medicine name:")

if query:
    results = df[df.apply(lambda row: query.lower() in row.astype(str).str.lower().values, axis=1)]
    
    if not results.empty:
        for idx, row in results.iterrows():
            st.markdown(f"### 🧾 {row['Brand']} ({row['Generic_Name']})")
            st.write(f"**Form:** {row['Form']} | **Strength:** {row['Strength']}")
            st.write(f"💰 **Brand Price:** ₹{row['Price_Brand']} | **Generic Price:** ₹{row['Price_Generic']}")
            st.write("🏥 **Available At:** " + row["Pharmacies"])
            st.success(f"💡 Save ₹{round(row['Price_Brand'] - row['Price_Generic'], 2)} by choosing the generic alternative!")
            st.markdown("---")
    else:
        st.error("Medicine not found. Try a different name.")
else:
    st.info("Please enter a medicine name above to begin.")

st.markdown("---")
st.markdown("⚠️ *This is a demo app. Always consult your doctor before switching medicines.*")
