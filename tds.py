import streamlit as st
import numpy as np

def largest_number(a, b, c):
    return max(a, b, c)

st.title("Find the largest among three numbers")
a = st.number_input("Enter the first number:")
b = st.number_input("Enter the second number:")
c = st.number_input("Enter the third number:")

if st.button("Find largest"):
    result = largest_number(a, b, c)
    st.success(f"The largest number is {result}")

