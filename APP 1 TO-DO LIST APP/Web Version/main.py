###The WEB Interface version of the TO-DO LIST APP
##Importing
import streamlit as st

from Backend import *

##Making the todo list
todos = read_todos()

##Adding title to the web app
st.title('My Todo app')
st.subheader("My First TO-DO APP")

##Adding elements:
# The checkboxes and list of the todos
for i in todos:
    st.checkbox(i)

# Input and label
st.text_input(label="", placeholder="Enter the TO-DO:")
