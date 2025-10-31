import pandas as pd
import streamlit as st


data = {
    "id": [1,2,3,4,5],
    "name": ["Swapnil Bankar", "Rahul Gandhile", "Rohan Bhopale", "Sumit Bankar", "Akash Bankar"],
    "salary": [50000, 60000, 45000, 30000, 55000]
}

df = pd.DataFrame(data)
st.write(df)