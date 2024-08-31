# import streamlit as st

# st.title("Hello, Streamlit!")
# st.write("This is a simple Streamlit app.")

# number = st.slider("Pick a number", 0, 100)
# st.write(f"The square of {number} is {number ** 2}.")
import streamlit as st
import pandas as pd
import numpy as np

st.title("Data Exploration with Streamlit")

# Create a random dataset
data = pd.DataFrame({
    'A': np.random.rand(100),
    'B': np.random.rand(100)
})

st.write("Here's a random dataset:")
st.dataframe(data)

st.write("Plotting a simple line chart:")
st.line_chart(data)

