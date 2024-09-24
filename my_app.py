import streamlit as st
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Title
st.title("My Streamlit App")

# Header
st.header("This is a header")

# Subheader
st.subheader("This is a subheader")

# Text
st.write("This is a normal text")

# Markdown
st.markdown("This is some **markdown** text")

# Markdown Stylings
st.markdown("I'm a **bold** text")
st.markdown("I'm an *italic* text")
st.markdown("I'm a [link](https://www.google.com)")

from PIL import Image

# Add an image from local file
image = Image.open('assets/zuck.png')
st.image(image, caption='This is an image')

# Add an image from the internet
image_url = 'https://www.thefamouspeople.com/profiles/images/elon-musk-1.jpg'
st.image(image_url, caption='This is an image from the internet')

# Simple graph
dates = pd.date_range('2024-01-01', periods=10)
trend = np.random.randn(10).cumsum()

# Line Chart using Matplotlib
def line_chart():
    # Defines the data used for our line chart, the markers used, line style, and the color
    plt.plot(dates, trend, marker='o', linestyle='-', color='b')
    plt.title('Line Chart Example')
    plt.xlabel('Date')
    plt.ylabel('Trend Value')
    # Rotates the dates shown in the x axis label (45 degrees) for readability
    plt.xticks(rotation=45) # rotate in 45 degrees
    # Display the plot in Streamlit
    st.pyplot(plt)
    # Removes the elements from this current figure so that it's ready for a new plot
    plt.clf()

line_chart()
st.write("this is a line chart")