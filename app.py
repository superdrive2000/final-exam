import streamlit as st
import joblib
import pandas as pd

# Cargar modelo
modelo = joblib.load("mlp_model_6features.pkl")
scaler = joblib.load("scaler.pkl")

# CSS para fondo y tarjetas
st.markdown("""
<style>
/* Imagen de fondo */
.stApp {
    background-image: url("fondo.jpg");  /* tu imagen local o URL */
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}

/* Tarjeta semitransparente para formulario y resultado */
.card {
    background-color: rgba(255, 255, 255, 0.85);
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0px 4px 20px rgba(0,0,0,0.3);
}

/* Botón centrado y estilizado */
div.stButton > button {
    display: block;
    margin: 0 auto;
    background-color: #28a745;
    color: white;
    font-size: 20px;
    font-weight: bold;
    padding: 10px 30px;
    border-radius: 12px;
    border: none;
}
div.stButton > button:hover {
    background-color: #218838;
}
</style>
""", unsafe_allow_html=True)

# Título principal
st.markdown("<h1 style='text-align:center; color:white;'>Predicción de Perfil de Horas</h1>", unsafe_allow_html=True)

# Layout con columnas: formulario izquierda, resultado derecha
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown('<div class="card">', unsafe_allow_html=True)  # Inicio tarjeta
    with st.form("formulario_prediccion"):
        tipo_farmacia = st.selectbox("Tipo de Farmacia", ["PROPIA", "FRANQUICIA"])
        venta_mensual = st.number_input("Venta mensual", min_value=0.0, step=1000.0)
        transacciones = st.number_input("Transacciones mensuales", min_value=0, step=100)
        headcount = st.slider("HeadCount", min_value=2, max_value=9, step=1)
        sucursal = st.selectbox("Sucursal", ["MEDICITY", "ECONOMICA"])
        cluster = st.number_input("Cluster", min_value=0, max_value=99, step=1)

        submitted = st.form_submit_button("Predecir Perfil de Horas")
    st.markdown('</div>', unsafe_allow_html=True)  # Fin tarjeta

with col2:
    st.markdown('<div class="card">', unsafe_allow_html=True)  # Inicio tarjeta resultado
    st.write("### Resultado")
    result_placeholder = st.empty()
    st.markdown('</div>', unsafe_allow_html=True)  # Fin tarjeta
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