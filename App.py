import streamlit as st
st.title('MPG ML Project')

displacement = st.number_input('Displacement', value=300)
horsepower = st.number_input('Horsepower', value=130)
Weight = st.number_input('weight', value=3000)
acceleration = st.number_input('acceleration', value= 12)
import pickle
loaded_model = pickle.load(open('mpg_regression.sav','rb'))