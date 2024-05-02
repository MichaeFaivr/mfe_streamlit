import streamlit as st
from vega_datasets import data
import matplotlib.pyplot as plt
import altair as alt
import numpy as np
from bokeh.plotting import figure
from bokeh.plotting import figure

source = data.cars()

st.title("Data Visualization web application")
st.header("Part 1: Data Exploration")
st.write("In this section, we will explore the Altair cars dataset.")
st.markdown("*Further resources [here](https://altair-viz.github.io/gallery/selection_histogram.html)*")

st.write(source)

slider = st.slider("Slider title", 0, 100, 50)
if slider > 80:
    st.write('STOOOOOP')
check = st.checkbox("Checkbox title", ["Add a constant", "Add beta 1", "Add beta 2"])
radio = st.radio("Radio title", ["Yes", "No"])
txt = st.text_input("Type here")
txt_area = st.text_area("Type here")
button = st.button("Button name")

choice = st.sidebar.radio("CHoisir" , ['Matplotlib', 'Altair', 'Bokeh'])

if choice == "Matplotlib":
    st.subheader("Matplotlib")
    plt.figure(figsize=(12,8))
    plt.scatter(source['Horsepower'], source['Miles_per_Gallon'])
    st.pyplot(plt)
elif choice == "Altair":
    st.subheader("Altair")
    brush = alt.selection(type='interval')
    points = alt.Chart(source).mark_point().encode(
        x='Horsepower:Q',
        y='Miles_per_Gallon:Q',
        color=alt.condition(brush, 'Origin:N', alt.value('lightgray'))
    ).add_params(
        brush
    )
    bars = alt.Chart(source).mark_bar().encode(
        y='Origin:N',
        color='Origin:N',
        x='count(Origin):Q'
    ).transform_filter(
        brush
    )
    st.altair_chart(points | (bars & bars))
else:   
    st.subheader("Bokeh")
    p = figure(title="First example")
    p.circle(source['Horsepower'], source['Miles_per_Gallon'])
    st.bokeh_chart(p)