import streamlit as st
import funciones

usuarios = [
    {'user': 'felipe', 'pass': 'felipe123'}, 
    {'user': 'cyan', 'pass': 'cyan123'}
]


st.title("Gestion de Blog")

accion = st.text_input("""
          Que desea hacer:
        #   1. salir del programa
          2. agregar usuario
          3. eliminar un post
          4. agrega un post
          5. lista todos tus post
          6. listar todos los post
        #   ------------------------
          """)
st.write(accion)

if accion == "2":
    usuario = st.text_input("digite un usuario: ")
    password = st.text_input("digite un password: ")
    funciones.create_user(usuario,password)

print(usuarios)