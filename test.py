import pandas as pd
from pandas import DataFrame as df
import streamlit as st
a = df(
        [
            [1, 2],
            [2, 15],
            [4, 34],
            [8, 50],
            [16, 65],
            [32, 70],
            [65, 84],
            ]
        )

a
st.write(a)
st.line_chart(a)


