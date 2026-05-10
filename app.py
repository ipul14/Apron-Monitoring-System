import streamlit as st
import os

st.set_page_config(
    page_title="Apron Monitoring System",
    page_icon="🛫",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.title("🛫 Apron Monitoring System - Weda Bay Airport")

# Path ke file HTML
html_path = "APRON SISTEM.html"

if os.path.exists(html_path):
    with open(html_path, "r", encoding="utf-8") as f:
        html_content = f.read()
    
    st.components.v1.html(
        html_content, 
        height=1400,      # Tinggi layar, bisa diubah
        scrolling=True
    )
else:
    st.error("❌ File HTML tidak ditemukan!")
    st.write("Pastikan nama file adalah `APRON SISTEM.html`")
