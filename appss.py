from turtle import color
import pandas as pd
import numpy as np
import pickle
import streamlit as st

from PIL import Image

# loading in the model to predict on the data
pickle_in = open('classifier.pkl', 'rb')
classifier = pickle.load(pickle_in)


def welcome():
    return 'Welcome all'

st.markdown("![Alt Text](https://acegif.com/wp-content/gifs/water-40.gif)")
def set_bg_hack_url():
   
        
    st.markdown(
         f"""
         <style>
         .stApp {{
             background: url("https://www.bing.com/th/id/OGC.052aee7320e8913fc7341a24fed5c1ab?pid=1.7&rurl=https%3a%2f%2fmedia2.giphy.com%2fmedia%2f3ohhwutQL0CDTq3kKA%2fsource.gif&ehk=x3uKysFnN%2ftJOhbjzdbY2FJybEyJZQqC952AGqyfn%2bA%3d");
             background-size: cover,align:center;
         }}
         </style>
         """,
         unsafe_allow_html=True
     )
set_bg_hack_url()


def prediction(ph,Hardness,Solids,Chloramines,Sulfate,Conductivity,Organic_carbon,Trihalomethanes,Turbidity):
    prediction = classifier.predict([[ph,Hardness,Solids,Chloramines,Sulfate,Conductivity,Organic_carbon,Trihalomethanes,Turbidity]])
    print(prediction)
    return prediction


# this is the main function in which we define our webpage
def main():
    # giving the webpage a title
    st.title("Water Potability")


    st.markdown('**Prediciting the Water Potability with following features that water is potable for drinking purpose or not. If water potability Output is 1 then water potable for drinking purpose whereas If Output is 0 then Water is Non- Potable.**') 
    # here we define some of the front end elements of the web page like
    # the font and background color, the padding and the text to be displayed
    html_temp = """
    <div style ="background-color:green;padding:13px">
    <h1 style ="color:black;text-align:center;">Streamlit Water Quality  </h1>
    </div>
        """
    
    
    st.markdown(html_temp, unsafe_allow_html = True)
    
    # the following lines create text boxes in which the user can enter
    # the data required to make the prediction
    ph = st.slider("Ph",min_value=0.00,max_value=14.00)
    Hardness = st.slider("Hardness", min_value=47.00,max_value=325.00)
    Solids = st.slider("Solids", min_value=320.00,max_value=61230.00)
    Chloramines = st.slider("Chloramines", min_value=0.30,max_value=13.20)
    Sulfate = st.slider("Sulfate", min_value=129.00,max_value=480.00)
    Conductivity = st.slider("Conductivity", min_value=181.00,max_value=755.00)
    Organic_carbon = st.slider("Organic_carbon",min_value=2.00,max_value=30.00)
    Trihalomethanes = st.slider("Trihalomethanes",min_value=0.00,max_value=124.00)
    Turbidity = st.slider("Turbidity",min_value=1.00,max_value=7.00)
    result =""
    
 
    
    if st.button("Predict"):
        result = prediction(ph,Hardness,Solids,Chloramines,Sulfate,Conductivity,Organic_carbon,Trihalomethanes,Turbidity)
        if (result==0):
            st.write("Water is Non-Potable")
        else:
            st.write("water is Potable")
    st.success('The Potability is {}'.format(result))
  
    # st.snow()
    
if __name__=='__main__':
    main()
