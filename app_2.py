# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 13:19:07 2025

@author: sindi
"""

import streamlit as st

st.title("Number selector ;)")

st.write("Hello, Streamlit!")

st.header("Number selection")

number = st.slider("Pick a number", 1, 100)
st.write(f"You picked: {number}")