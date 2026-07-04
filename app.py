from llm.ai_pipeline import classify_material
from listings.demo_listing import listing
import streamlit as st
import json

st.title("ReMatter — Demo")
st.write(listing)

if st.button("Run ReMatter Pipeline"):
    response = classify_material(listing["material_description"]).replace("```json", "").replace("```", "").strip()
    result = json.loads(response)
    st.subheader("Classification")
    st.json(result)
    # then call match_buyers, estimate_value, estimate_carbon_saved and display