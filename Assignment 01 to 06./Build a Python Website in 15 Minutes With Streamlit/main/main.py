import streamlit as st

# Title of the app
st.title('My First Streamlit App')

# Text in the app
st.write('Hello, Streamlit! This is a basic website built in Python using Streamlit.')

# A simple input field
name = st.text_input("What's your name?")
if name:
    st.write(f"Hello, {name}!")

# A slider to choose a number
number = st.slider("Pick a number", 0, 100)
st.write(f'You selected: {number}')

# A simple button interaction
if st.button('Click me'):
    st.write('You clicked the button!')

# Display a simple plot
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_title('A simple plot')

st.pyplot(fig)

