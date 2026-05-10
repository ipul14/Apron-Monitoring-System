import streamlit as st
import os

st.set_page_config(
    page_title="Apron Monitoring System",
    page_icon="🛫",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.title("🛫 Apron Monitoring System - Weda Bay Airport")
st.caption("Weda Bay Airport • PT. Indonesia WedaBay Industrial Park")

# Path ke file HTML
html_path = "apron/apron_system.html"

if os.path.exists(html_path):
    with open(html_path, "r", encoding="utf-8") as f:
        html_content = f.read()
    
    st.components.v1.html(
        html_content, 
        height=1450,      # Sesuaikan tinggi sesuai kebutuhan
        scrolling=True
    )
else:
    st.error("❌ File HTML tidak ditemukan!")
    st.write(f"Path yang dicari: `{html_path}`")
    st.write("Cek apakah file `apron/apron_system.html` sudah ada.")
