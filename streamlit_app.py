from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

"""
# Welcome to Streamlit!
Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:
If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).
In the meantime, below is an example of what you can do with just a few lines of code:
"""


with st.echo(code_location='below'):
    lat = st.text_input(label="Latitude", value="41.015137")
    lon = st.text_input(label="Longitude", value="28.979530")
    # 41.015137, 28.979530
    df = pd.DataFrame(
         {"lat":[float(lat)], "lon":[float(lon)]})

    st.map(df)
