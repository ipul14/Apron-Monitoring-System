import streamlit as st

st.set_page_config(
    page_title="Apron Monitoring System",
    page_icon="🛫",
    layout="wide"
)

st.title("🛫 Apron Monitoring System - Weda Bay Airport")
st.caption("Weda Bay Airport • PT. Indonesia WedaBay Industrial Park")

html_path = "apron/apron_system.html"

if st.button("🔄 Refresh / Load Ulang"):
    st.rerun()

if st.checkbox("Tampilkan HTML", value=True):
    try:
        with open(html_path, "r", encoding="utf-8") as f:
            html_content = f.read()
        
        st.components.v1.html(
            html_content, 
            height=1600,      # Naikkan tinggi
            scrolling=True,
            width=None
        )
    except Exception as e:
        st.error(f"Error: {e}")
else:
    st.info("Centang kotak di atas untuk menampilkan sistem")
