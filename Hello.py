# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="Search",
        page_icon="👋",
    )

    st.title("PathoGeneMap")
    #merge weseley's code and put it on this page
    st.markdown("### *Empowering biomedical researchers with AI-enhanced exploration of disease causing genes.*")
    st.write("Imagine a future in drug discovery where decisions are made not by chance, but through precision and data. Introducing PathoGeneMap—a groundbreaking tool that uses AI to navigate the complex landscape of disease-causing genes. The biomedical field is rich with experiments outlining genes’ roles in diseases, yet this critical information is locked away in dense literature. My experience as an MDPhD, manually reviewing 3,000 abstracts for data on just 100 genes, highlights the daunting task researchers face. PathoGeneMap addresses this challenge by leveraging AI to sift through 35 million biomedical papers to present the exact information researchers need. PathoGeneMap empowers researchers worldwide to make informed decisions, accelerating the development of new treatments for patients.")
    
if __name__ == "__main__":
    run()
