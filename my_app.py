import streamlit as st
from PIL import Image
import matplotlib.pyplot as plt

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

# Markdown Stylings
st.markdown("I'm a **bold** text")
st.markdown("I'm an *italic* text")
st.markdown("I'm a [link](https://www.google.com)")

# Add an image from local file
image = Image.open('assets/zuck.png')
st.image(image, caption='This is an image')

# Add an image from the internet
image_url = 'https://www.thefamouspeople.com/profiles/images/elon-musk-1.jpg'
st.image(image_url, caption='This is an image from the internet')
# Simple graph
fig, ax = plt.subplots()
ax.plot([1, 2, 3, 4, 5])
st.pyplot(fig)
st.write("This is a line graph")