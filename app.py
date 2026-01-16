import streamlit as st
import pandas as pd
import pickle
import numpy as np
 
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

st.set_page_config(layout="wide")
st.title("🛡️ Application de Prédiction du Risque")
st.write("Ajustez les paramètres ci-dessous pour évaluer le niveau de risque.")

st.subheader("📋 Profil du Client")

col1, col2, col3, col4 = st.columns(4)
with col1: a1 = st.slider('A1', 13.75, 80.25, 31.56)
with col2: a2 = st.slider('A2', 0.0, 28.0, 4.75)
with col3: a3 = st.slider('A3', 0.0, 2000.0, 184.01)
with col4: a4 = st.slider('A4', 0.0, 100000.0, 5.0)

cat_col1, cat_col2, cat_col3 = st.columns(3)
with cat_col1: a5 = st.selectbox('A5', ('g', 'p', 'gg'))
with cat_col2: a6 = st.selectbox('A6', ('c', 'q', 'w', 'i', 'aa', 'ff', 'k', 'cc', 'x', 'm', 'd', 'e', 'j', 'r'))
with cat_col3: a7 = st.selectbox('A7', ('v', 'h', 'bb', 'ff', 'j', 'z', 'dd', 'n', 'o'))

df_input = pd.DataFrame({'A1': [a1], 'A2': [a2], 'A3': [a3], 'A4': [a4], 'A5': [a5], 'A6': [a6], 'A7': [a7]})


num_cols = ['A1', 'A2', 'A3', 'A4']
df_input[num_cols] = np.log1p(df_input[num_cols])

df_raw = pd.read_excel("Risque_data.xlsx")
X_raw = df_raw.drop('Risque', axis=1)
df_encoded = pd.get_dummies(df_input)
X_final = df_encoded.reindex(columns=pd.get_dummies(X_raw).columns, fill_value=0)

st.markdown("---")
if st.button('🚀 Lancer la Prédiction', use_container_width=True):
   
    prediction = model.predict(X_final)
    prediction_proba = model.predict_proba(X_final)
    
    res_col1, res_col2 = st.columns(2)
    with res_col1:
        risk_label = "Risque Elevé" if prediction[0] == 1 else "Risque Faible"
        if prediction[0] == 1:
            st.error(f"### Résultat : {risk_label}")
        else:
            st.success(f"### Résultat : {risk_label}")
            
    with res_col2:
        conf = np.max(prediction_proba) * 100
        st.metric("Niveau de Confiance", f"{conf:.2f}%")
        st.progress(int(conf))

