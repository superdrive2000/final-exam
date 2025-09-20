import streamlit as st
import joblib
import pandas as pd

# Cargar modelo
modelo = joblib.load("mlp_model_6features.pkl")
scaler = joblib.load("scaler.pkl")

# CSS para fondo e interfaz
page_bg = """
<style>
/* Imagen de fondo */
.stApp {
    background-image: url("fondo.jpg");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}

/* Centrar y estilizar botón */
div.stButton > button {
    display: block;
    margin: 0 auto;  /* Centrado */
    background-color: #28a745; /* Verde */
    color: white;
    font-size: 20px;  /* Más grande */
    font-weight: bold;
    padding: 10px 30px;
    border-radius: 12px;
    border: none;
}
div.stButton > button:hover {
    background-color: #218838; /* Verde más oscuro al pasar mouse */
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)


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
    
    pd.DataFrame([nueva_farmacia])

    nuevo_farmacia = scaler.transform(pd.DataFrame([nueva_farmacia]))

    # Hacemos una predicción de la especie del 'nuevo_pinguino' con el método 'predict' del modelo 'mlp'
    # Guardamos la predicción en la variable 'nueva_prediccion'
   
    
    perfil_horas = modelo.predict(nueva_farmacia)

    st.success(f"El Perfil de Horas estimado es: **{perfil_horas}**")