import streamlit as st

st.title("Roteiro 1: Primeiros Passos com Streamlit")

st.text_input("Digite algo", key="input_text")

if st.button("Clique-me"):
    st.write(st.session_state.input_text)
