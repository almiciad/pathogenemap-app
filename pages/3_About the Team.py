import streamlit as st
from streamlit.hello.utils import show_code


st.set_page_config(page_title="Meet the Team", page_icon="📹")
st.markdown("# Meet the Team")
st.sidebar.header("Meet the Team")
st.write(
    """The team is comprised of 5 engineers. Wesley Chang,
    Almicia Dunson,
    Andrew Mcall,
    Max Kaufman, and
    Christian Lee. 

    Here is a small insert about what each person contributed to the project. 

    Here is the teams contact information. 
    """
)