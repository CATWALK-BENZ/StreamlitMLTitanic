#import libraries
import streamlit as st
from joblib import load

#st.title('Hello World')
model = load('titanic_model.joblib')

#Create streamlit webapp
st.title('Titanic survival prediction')
#side bar with menu
st.sidebar.title('Menu')
#menu option
menu = ['Home','Prediction']
#Sidebar selection
st.sidebar.selectbox('',menu)
#input with sliders
age = st.slider('Age',0.42,80.0,30.0)
sibsp = st.slider('Sibsp',0,8,0)
parch = st.slider('Parch',0,9,0)
fare = st.slider('Fare',0.0,512.30,32.20)
#Add precition button
predict_button = st.button('Predict')
#Prediction logic
if predict_button:
    input_data =[[age,sibsp,parch,fare]]
   #Prediction
    prediction = model.predict(input_data)
    #หาค่าความน่าจะเป็น
    predict_proba = model.predict_proba(input_data)
    #disply
    st.subheader('Prediction')
    if prediction[0] ==1:
        st.write('Survived')
    else:
        st.write('Not Survived')
   #แสดงความน่าจะเป็น
    st.subheader('Prediction Probability')
    st.write(f'Survived: {predict_proba[0][1]:.2f}')
    st.write(f'Not Survived: {predict_proba[0][0]:.2f}')
