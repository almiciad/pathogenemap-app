import streamlit as st
from streamlit.hello.utils import show_code


st.set_page_config(page_title="Meet the Team", page_icon="📹")
st.markdown("# Meet the Team")
st.sidebar.header("Meet the Team")

#need to make every photo the same size
andrew = '/workspaces/pathogenemap-app/pages/photots/Screenshot 2024-03-12 at 9.11.25 AM.png'
christian = '/workspaces/pathogenemap-app/pages/photots/Screenshot 2024-03-12 at 9.11.36 AM.png'
max = '/workspaces/pathogenemap-app/pages/photots/Screenshot 2024-03-12 at 9.11.48 AM.png'
wesley = '/workspaces/pathogenemap-app/pages/photots/Screenshot 2024-03-12 at 9.12.01 AM.png'
almicia = '/workspaces/pathogenemap-app/pages/photots/Screenshot 2024-03-12 at 9.12.14 AM.png'

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### Wesley Chang")
    st.image(wesley)
    st.write("""this is a short bio for [name]. [name] contributed to the [role] piece of this project
            Here is one more sentence about [name]. And a closing sentence for good measure. """)
    st.markdown("### Almicia Dunson")
    st.image(almicia)
    st.write("""this is a short bio for [name]. [name] contributed to the [role] piece of this project
            Here is one more sentence about [name]. And a closing sentence for good measure. """)
    
   

with col2:
    st.markdown("### Andrew Mcall")
    st.image(andrew) 
    st.write("""this is a short bio for [name]. [name] contributed to the [role] piece of this project
            Here is one more sentence about [name]. And a closing sentence for good measure. """)
    st.markdown("### Max Kaufman")
    st.image(max)
    st.write("""this is a short bio for [name]. [name] contributed to the [role] piece of this project
            Here is one more sentence about [name]. And a closing sentence for good measure. """)

with col3:
    st.markdown("### Christian Lee")
    st.image(christian)
    st.write("""this is a short bio for [name]. [name] contributed to the [role] piece of this project
            Here is one more sentence about [name]. And a closing sentence for good measure. """)



   
    
