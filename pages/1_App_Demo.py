import streamlit as st
import altair as alt
import pandas as pd
from urllib.error import URLError

from streamlit.hello.utils import show_code


st.set_page_config(page_title="App Demo", page_icon="📹")
st.markdown("# App Demo")
st.sidebar.header("App Demo")
st.write(
    """Choose a gene to see related information.
    """
)

genes_data = pd.read_csv("https://raw.githubusercontent.com/wesleywchang/2024-capstone-gene-nlp/main/fine_tuning_dataset/fine_tuning_dataset_v1.2/finetuning_training_data/processed/in_vivo_gene_perturbations_test_sample1k_random.csv?token=GHSAT0AAAAAACMV4AR5P7IUZIB5K4RVCZEWZPQSYLQ")

bygenes = genes_data.set_index(['label'])
gp = st.selectbox("Choose label", list(bygenes.index))
st.write("You selected:", gp)
gpdata = bygenes.loc[gp]
st.write(bygenes.sort_index())



