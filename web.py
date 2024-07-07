import streamlit as st
import functions
todos = functions.get_todos()


def add_todo():
    todo = st.session_state["new_todo"] + '\n'
    todos.append(todo)
    functions.write_todos(todos)


st.title("My To-do App")
st.subheader("This is just a simple to-do app that makes a list.")
st.write("Add a new todo below or check a checkbox to remove it from the list.")


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="Enter a todo", label_visibility='hidden',
              placeholder="Add new todo...",
              on_change=add_todo, key='new_todo')