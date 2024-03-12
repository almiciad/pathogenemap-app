import streamlit as st
from streamlit.hello.utils import show_code


st.set_page_config(page_title="EDA", page_icon="📹")
st.markdown("# EDA")
st.sidebar.header("EDA")
st.write(
    """Here is a description of our dataset and how it came to be. 
    There are also graphs and charts that provide quick stats on our dataset on this page. 
    """
)