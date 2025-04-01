
import streamlit as st
import pandas as pd
from PIL import Image
import requests
from io import BytesIO
from batch_prompt_generator import generate_batch

st.set_page_config(page_title="AI Prompt Generator", layout="wide")

st.image("HBR.jpg", width=200)
st.title("🧠 AI Batch Prompt Generator for Commercial Use")

st.markdown("### 📝 Input Concepts")
concepts_input = st.text_area("Enter concepts (one per line)", height=150)
category = st.selectbox("Select Image Category", ["Fashion", "Skincare", "Business", "Lifestyle"])
batch_size = st.slider("Number of Prompts", 1, 20, 6)

if st.button("🚀 Generate Batch Prompts"):
    concepts = [c.strip() for c in concepts_input.split("\n") if c.strip()]
    if not concepts:
        st.warning("Please input at least one concept.")
    else:
        df = generate_batch(concepts, category, batch_size)

        for i, row in df.iterrows():
            st.markdown(f"---\n### 🔹 {row['Title']}")
            st.write("**Prompt:**", row["Prompt"])
            st.write("**Image Description:**", row["Image Description"])
            st.write("**Keywords:**", row["Keywords"])
            st.write("**Suggestions:**", row["Suggestions"])

            if row["Reference"]:
                try:
                    img_data = requests.get(row["Reference"], timeout=3).content
                    img = Image.open(BytesIO(img_data))
                    st.image(img, caption="Reference Preview", use_column_width=True)
                except:
                    st.markdown(f"[🔗 View Reference]({row['Reference']})")

        st.download_button("⬇️ Download CSV", df.to_csv(index=False), file_name="ai_prompts_batch.csv")
