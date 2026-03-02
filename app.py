import streamlit as st
import tempfile
from orchestration.graph import run_pipeline

st.set_page_config(page_title="Slide Agent", layout="wide")

st.title("AI Slide Generator Agent")

prompt = st.text_area(
    "Describe the presentation you want",
    height=150,
    placeholder="Create a 5 slide investor deck with revenue chart"
)

if st.button("Generate Presentation"):

    if not prompt.strip():
        st.warning("Please enter a prompt.")
        st.stop()

    with st.spinner("Agent is generating slides..."):

        try:
            output_path = run_pipeline(prompt)

            st.success("Presentation generated!")

            with open(output_path, "rb") as f:
                st.download_button(
                    label="Download PPTX",
                    data=f,
                    file_name="generated_presentation.pptx",
                    mime="application/vnd.openxmlformats-officedocument.presentationml.presentation"
                )

        except Exception as e:
            st.error("Generation failed")
            st.code(str(e))