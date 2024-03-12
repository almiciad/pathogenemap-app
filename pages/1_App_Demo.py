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

def data_frame_demo():
    @st.cache_data
    def get_UN_data():
        DATA_URL = "https://raw.githubusercontent.com/wesleywchang/2024-capstone-gene-nlp/main/fine_tuning_dataset/fine_tuning_dataset_v1.2/finetuning_training_data/processed/in_vivo_gene_perturbations_test_sample1k_random.csv?token=GHSAT0AAAAAACMV4AR5P7IUZIB5K4RVCZEWZPQSYLQ"
        df = pd.read_csv(DATA_URL)
        return df.set_index("label")

    try:
        df = get_UN_data()
        countries = st.multiselect(
            "Choose perbutation", list(df.index)
        )
        if not countries:
            st.error("Please select at least one country.")
        else:
            data = df.loc[countries]
            #data /= 1000000.0
            st.write("### Gene Information", data.sort_index())
    except URLError as e:
        st.error(
            """
            **This demo requires internet access.**
            Connection error: %s
        """
            % e.reason
        )

data_frame_demo()

