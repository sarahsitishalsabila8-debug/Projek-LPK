import streamlit as st

t.set_page_config(
page_title="FinanceDashboard",
layout="wide"
)

st.title("📊Dashboard")
st.header("LaporanBulanan")
st.subheader("📈MonthlyExpenses")
st.caption("Madewith❤usingStreamlit")

title = st.text_input("Movie title", "Life of Brian")
st.write("The current movie title is", title)

st.button("Reset", type="primary")
if st.button("Say hello"):
    st.write("Why hello there")
else:
    st.write("Goodbye")
  
