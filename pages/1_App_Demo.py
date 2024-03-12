import streamlit as st
import altair as alt
import pandas as pd
from urllib.error import URLError

from streamlit.hello.utils import show_code


st.set_page_config(page_title="App Demo", page_icon="📹")
st.markdown("# App Demo")
st.sidebar.header("App Demo")
st.write(
    """This page has the actual demo and the database connection. 
    """
)

def demo():
    @st.cache_data
    def get_data():
        #replace AWS bucket and csv name
        AWS_BUCKET_URL = "https://streamlit-demo-data.s3-us-west-2.amazonaws.com"
        df = pd.read_csv("https://github.com/wesleywchang/2024-capstone-gene-nlp/blob/main/fine_tuning_dataset/fine_tuning_dataset_v1.2/finetuning_training_data/processed/in_vivo_gene_perturbations_test_sample1k_random.csv")
        return df.set_index("id")
    
    data = get_data()

    

demo()

#show_code(dademo)