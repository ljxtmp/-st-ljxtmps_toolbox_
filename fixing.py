import streamlit as st

def fixing():
    page = st.sidebar.radio('我的主页', ['首页', '我的兴趣推荐', '计算器', '图片处理工具', '智慧词典', '网址导航', 'RGB调色板', '留言区'])
    st.write(page)
    st.write('')
    st.write('网站维护中…')
