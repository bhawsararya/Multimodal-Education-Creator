import streamlit as st
from llm import generate_explanation
from image_gen import generate_image
# from vector_db import add_to_vector_db, search_vector_db

st.set_page_config(page_title="Multimodal Education Creator", layout="wide")

st.title("📚 Multimodal Education Creator")
topic = st.text_input("Enter an Educational Concept")

if st.button("Generate Learning Content"):
    if topic:
        # Generate explanation
        with st.spinner("Generating explanation..."):
            explanation = generate_explanation(topic)
        # add_to_vector_db(explanation)

        # Only generate image if explanation is valid
        if "Sorry, this topic is not supported" not in explanation:
            with st.spinner("Generating visual (fast diffusion)..."):
                image = generate_image(topic)
        else:
            image = None  # Skip image generation

        # Display results safely
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("### 📖 Explanation")
            st.write(explanation)

        with col2:
            st.markdown("### 🖼️ Visual")
            if image:
                st.image(image)
            else:
                st.info("No visual generated for this topic.")

# st.markdown("---")

# query = st.text_input("Search Similar Concepts")
# if st.button("Search"):
#     results = search_vector_db(query)
#     if results:
#         st.write(results[0])
#     else:
#         st.info("No data found.")