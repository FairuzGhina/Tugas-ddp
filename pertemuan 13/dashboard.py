import streamlit as  st

st.title("Ini halaman Dashboard!")
st.session_state['Nabung']

jumlah = 0
for session in st.session_state['Nabung']:
    jumlah += session['Nominal']
    
st.write("Total nominal menabung sebesar", jumlah)