import streamlit as st
import os

st.set_page_config(
    page_title="Apron Monitoring System",
    page_icon="🛫",
    layout="wide"
)

st.title("🛫 Apron Monitoring System - Weda Bay Airport")
st.caption("Weda Bay Airport • PT. Indonesia WedaBay Industrial Park")

html_path = "apron/apron_system.html"

if os.path.exists(html_path):
    # Baca file sebagai raw HTML
    with open(html_path, "r", encoding="utf-8") as f:
        html_content = f.read()
    
    # Tampilkan menggunakan iframe (lebih stabil untuk HTML besar)
    st.components.v1.iframe(
        srcdoc=html_content,
        height=1600,
        scrolling=True
    )
else:
    st.error("File HTML tidak ditemukan")
    st.write("Path:", html_path)
