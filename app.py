import streamlit as st
import joblib
import pandas as pd

# Cargar modelo
modelo = joblib.load("mlp_model_6features.pkl")
scaler = joblib.load("scaler.pkl")

# Título
st.title("Predicción de Perfil de Horas")

# Simular fondo con st.image
st.image("fondo.jpg", use_column_width=True, output_format="auto")

st.write("## Complete el formulario:")

# Layout con columnas: formulario a la izquierda, resultado a la derecha
col1, col2 = st.columns([2, 1])

with col1:
    with st.form("formulario_prediccion"):
        tipo_farmacia = st.selectbox("Tipo de Farmacia", ["PROPIA", "FRANQUICIA"])
        venta_mensual = st.number_input("Venta mensual", min_value=0.0, step=1000.0)
        transacciones = st.number_input("Transacciones mensuales", min_value=0, step=100)
        headcount = st.slider("HeadCount", min_value=2, max_value=9, step=1)
        sucursal = st.selectbox("Sucursal", ["MEDICITY", "ECONOMICA"])
        cluster = st.number_input("Cluster", min_value=0, max_value=99, step=1)

        # Botón centrado y grande usando columnas internas
        btn_col1, btn_col2, btn_col3 = st.columns([1,2,1])
        with btn_col2:
            submitted = st.form_submit_button("Predecir Perfil de Horas")
            
with col2:
    st.write("### Resultado")
    result_placeholder = st.empty()  # Aquí se mostrará la predicción

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

    result_placeholder.success(f"El Perfil de Horas estimado es: **{perfil_horas[0]}**")