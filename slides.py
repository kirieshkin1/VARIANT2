import streamlit as st
import reveal_slides as rs

with open("slides_intro1.md", "r", encoding="utf-8") as f:
    slides_content = f.read()

rs.slides(content=slides_content,theme="solarized",  # Тема с хорошей подсветкой кода
    height=600,
    config={
        "controls": True,
        "progress": True,
        "center": True,
        "transition": "slide"
    })
st.markdown(
    """
    <style>
    .reveal pre code {
        font-size: 1.2em;  /* Увеличение размера шрифта кода */
        line-height: 1.4;  /* Улучшение межстрочного интервала */
        background-color: #f8f8f8;  /* Светлый фон для кода */
        padding: 10px;  /* Отступы внутри блока кода */
    }
    </style>
    """,
    unsafe_allow_html=True
)