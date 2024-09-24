import streamlit as st 
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


st.write("hello world")

st.write("this is a new line")

# Markdowns

st.markdown("This is a **bold** text") # ** your text **
st.markdown("This is a *italic* text") # * your text *
st.markdown("I'm a [link](https://google.com)") # [the text link](the actual URL / link)

# Titles, Headers, Subheaders

st.title("Your title")
st.header("This is a header")
st.subheader("This is a subheader")

st.write("this is a normal text")

# Images

local_image = Image.open("assets/zuck.png")
st.image(local_image, caption="Mark Zuckerberg")

image_url = "http://www.thefamouspeople.com/profiles/images/elon-musk-1.jpg"
st.image(image_url, caption="Elon Musk")

# GRAPHS

# Dummy Data Generation
dates = pd.date_range('2024-01-01', periods=10)
trend = np.random.randn(10).cumsum()
categories = ['A', 'B', 'C', 'D']
values = np.random.randint(10, 100, size=4)

# Line Chart
def line_chart():
  # Defines the data used for our line chart, the markers used, line style, and the color
  plt.plot(dates, trend, marker='o', linestyle='-', color='b')
  plt.title('Line Chart Example')
  plt.xlabel('Date')
  plt.ylabel('Trend Value')
  # Rotates the dates shown in the x axis label (45 degrees) for readability
  plt.xticks(rotation=45) # rotate in 45 degrees

  st.pyplot(plt)
  plt.clf()

st.subheader("Line Chart")
line_chart()

# Bar Chart using Matplotlib
def bar_chart():
  colors = ['skyblue', 'lightgreen', 'salmon', 'orange']  # you can define colors using a list

  # defines the cateogries, values, and the color for our chart
  plt.bar(categories, values, color=colors)
  # this displays a Title for our chart
  plt.title('Bar Chart Example')
  # this defines the label for the y axis of our chart
  plt.ylabel('Value')
  # this defines the label for the x axis of our chart
  plt.xlabel('Categories')
  # this shows the graph
  st.pyplot(plt)
  plt.clf()

bar_chart()