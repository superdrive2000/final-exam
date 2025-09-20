import streamlit as st
import joblib
import pandas as pd

# Cargar modelo
modelo = joblib.load("mlp_model_6features.pkl")
scaler = joblib.load("scaler.pkl")

# Imagen de fondo simulada
st.image("fondo.jpg", use_column_width=True)


# Título de la app
st.title("Predicción de Perfil de Horas")
st.write("Complete el siguiente formulario para obtener el perfil de horas de la farmacia.")

# Formulario
with st.form("formulario_prediccion"):
    tipo_farmacia = st.selectbox("Tipo de Farmacia", ["PROPIA", "FRANQUICIA"])
    sucursal = st.selectbox("Sucursal", ["MEDICITY", "ECONOMICAS"])
    venta_mensual = st.number_input("Venta mensual", min_value=0.0, step=1000.0)
    transacciones = st.number_input("Transacciones mensuales", min_value=0, step=100)
    headcount = st.slider("HeadCount", min_value=2, max_value=9, step=1)
    cluster = st.number_input("Cluster", min_value=0, max_value=99, step=1)

    # Botón para enviar
    submitted = st.form_submit_button("Predecir Perfil de Horas")

# Predicción
if submitted:
    tipo_farmacia_val = 0 if tipo_farmacia == "PROPIA" else 1
    sucursal_val = 0 if sucursal == "ECONOMICAS" else 1   
    
    nueva_farmacia = [tipo_farmacia_val, venta_mensual, transacciones,
                   headcount, sucursal_val, cluster]


    nueva_farmacia = scaler.transform(pd.DataFrame([nueva_farmacia]))

    # Hacemos una predicción de la especie del 'nuevo_pinguino' con el método 'predict' del modelo 'mlp'
    # Guardamos la predicción en la variable 'nueva_prediccion'
   
    
    perfil_horas = modelo.predict(nueva_farmacia)

    st.success(f"El Perfil de Horas estimado es: **{perfil_horas[0]}**")