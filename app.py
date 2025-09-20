import streamlit as st

# Título de la app
st.title("Predicción de Perfil de Horas")
st.write("Complete el siguiente formulario para obtener el perfil de horas de la farmacia.")

# Formulario
with st.form("formulario_prediccion"):
    tipo_farmacia = st.selectbox("Tipo de Farmacia", ["PROPIA", "FRANQUICIA"])
    venta_mensual = st.number_input("Venta mensual", min_value=0.0, step=1000.0)
    transacciones = st.number_input("Transacciones mensuales", min_value=0, step=100)
    headcount = st.slider("HeadCount", min_value=2, max_value=9, step=1)
    sucursal = st.selectbox("Sucursal", ["MEDICITY", "ECONOMICA"])
    cluster = st.number_input("Cluster", min_value=0, max_value=99, step=1)

    # Botón para enviar
    submitted = st.form_submit_button("Predecir Perfil de Horas")