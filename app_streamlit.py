import streamlit as st
from recommender import recommend_assessments

st.title("SHL Assessment Recommendation System")
query = st.text_input("Enter Job Description or URL:")

if st.button("Get Recommendations"):
    results = recommend_assessments(query)
    for rec in results:
        st.markdown(f"**[{rec['name']}]({rec['url']})** - {rec['duration']} ({rec['type']})")
