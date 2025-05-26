import streamlit as st
from PIL import Image
from utils import extract_feature_vector, find_similar_outfits, generate_fashion_advice

st.set_page_config(page_title="TrendTailor AI", layout="centered")
st.title("👗 TrendTailor AI – Outfit Matcher & Fashion Advice")

uploaded_file = st.file_uploader("Upload a fashion item image (top, jeans, etc.)", type=["jpg", "jpeg", "png"])

if uploaded_file:
    img = Image.open(uploaded_file)
    st.image(img, caption="Uploaded Item", use_column_width=True)

    st.subheader("🔍 Finding Outfit Matches...")
    vec = extract_feature_vector(img)
    matches = find_similar_outfits(vec)

    for match_file, score in matches:
        st.image(f"outfits/{match_file}", caption=f"Match: {match_file} (Score: {round(score, 2)})")

    st.subheader("🧠 Fashion Advice")
    item_type = st.selectbox("Select the item category", ["Top", "Bottom", "Dress", "Jacket", "Other"])
    advice = generate_fashion_advice(item_type)
    st.markdown(f"💡 **Tip:** {advice}")
