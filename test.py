import joblib
import pandas as pd

# Cargar modelo
modelo = joblib.load("mlp_model_6features.pkl")
scaler = joblib.load("scaler.pkl")



nueva_farmacia = [ 0,26109, 2159, 4,0,33]
nueva_farmacia = scaler.transform(pd.DataFrame([nueva_farmacia]))

# Hacemos una predicción de la especie del 'nuevo_pinguino' con el método 'predict' del modelo 'mlp'
# Guardamos la predicción en la variable 'nueva_prediccion'

    
perfil_horas = modelo.predict(nueva_farmacia)

print(perfil_horas)