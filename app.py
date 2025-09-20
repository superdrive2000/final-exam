import streamlit as st

st.title("Formulario Básico")

with st.form("formulario_basico"):
    nombre = st.text_input("Nombre")
    email = st.text_input("Correo electrónico")
    edad = st.number_input("Edad", min_value=0, max_value=120, step=1)
    enviado = st.form_submit_button("Enviar")

    if enviado:
        st.success(f"¡Formulario enviado!\nNombre: {nombre}\nCorreo: {email}\nEdad: {edad}")
        