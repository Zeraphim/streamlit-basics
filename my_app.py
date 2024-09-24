import streamlit as st

# Title
st.title("My Streamlit App")

# Header
st.header("This is a header")

# Subheader
st.subheader("This is a subheader")

# Text
st.write("This is some text")

# Markdown
st.markdown("This is some **markdown** text")


import matplotlib.pyplot as plt

# Simple graph
fig, ax = plt.subplots()
ax.plot([1, 2, 3, 4, 5])
st.pyplot(fig)