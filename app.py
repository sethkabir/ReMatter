from llm.ai_pipeline import classify_material
from listings.demo_listing import listing
from buyers.buyers import match_buyers, buyers
import streamlit as st
import json

st.title("ReMatter — Demo")
st.write(listing)

if st.button("Run ReMatter Pipeline"):
    #Calling classification
    response = classify_material(listing["material_description"]).replace("```json", "").replace("```", "").strip()
    result = json.loads(response)
    st.subheader("Classification")
    st.json(result)

    #Calling buyers
    response2 = match_buyers(listing,"leather", buyers)
    result2 = response2
    st.subheader("Potential buyers")
    st.json(result2)