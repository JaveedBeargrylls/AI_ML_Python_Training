
import joblib
import streamlit as st

model=joblib.load(r"C:\Training\AI_ML_Python_Training\Day05\ccpp_model.pkl")

# test=[[23.45,45.56,1015,34.456]]

# print(model.predict(test))

#####

st.title("CCPP Model")
st.subheader("predicting Energy Output based on feature like temperature, pressure, vaccum and humidity")

temp=st.number_input("enter temperatue value")
humi=st.number_input("enter humi value")
pressure=st.number_input("enter pressure value")
vacc=st.number_input("enter vaccume value")

data=[[temp,humi,pressure,vacc]]

if st.button("Enter"):
    output=model.predict(data)
    st.success(f"Predicted Energy Output : {str(output[0])}")