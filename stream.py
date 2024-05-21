import streamlit as st
import pandas as pd

st.title("Welcome to LLMS")
st.header('Machine Learning')
st.subheader("building apps with llms ")

st.title('list of the people ')

data = {
    'Name': ['James', 'Anar', 'Gayathri', 'David'],
    'Age': [44, 38, 18, 32],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}
df = pd.DataFrame(data)

# Display the dataframe as a table
st.table(df)
