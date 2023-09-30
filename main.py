###The WEB Interface version of the TO-DO LIST APP
##Importing
import streamlit as st

import Backend

##Making the todo list
todos = Backend.read_todos()


def add_todo():
    t = st.session_state["new_todo"] + "\n"
    todos.append(t)
    Backend.modifying_todo(todos)


##Adding title to the web app
st.title('My Todo app')
st.subheader("My First TO-DO APP")

##Adding elements:
# The checkboxes and list of the todos
for todo in todos:
    st.checkbox(todo)

# Input and label
st.text_input(label="Enter the TO-DO:", placeholder="Enter the TO-DO:",
              on_change=add_todo, key='new_todo')

st.session_state
