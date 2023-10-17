import streamlit as st
import pandas as pd

st.title("Roteiro 2: Widgets Interativos")

value = st.slider("Escolha um valor", 0, 100)

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
    })

option = st.selectbox('Escolha um numero',
     df['first column'])

radio = st.radio('Escolha um numero', df['second column'])

toggle = st.toggle('toglle')

select_box = st.checkbox('selecione')

if st.button("Mostrar valor do slider"):
    st.write(f"Valor escolhido: {value, option, radio, select_box}")

