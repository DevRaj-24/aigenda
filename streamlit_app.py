import streamlit as st 
import os
from PIL import Image 
import google.generativeai as genai

genai.configure(api_key="AIzaSyBOVcHQEEYyGfl3Wc34GSVb2x6YRVq9vgQ")

model=genai.GenerativeModel('gemini-1.5-flash')

def get_gemini_response(input_text,image_data,prompt):
    response=model.generate_content([input_text,image_data[0],prompt])
    return response.text

def input_image_details(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        image_parts=[
            {
                'mime_type':uploaded_file.type,
                "data":bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError('no file was uploaded')
    
st.set_page_config(page_title="DEV RAJ INVOICE GENERATOR")
st.sidebar.header("RoboBILL")
st.sidebar.write("Made by Dev Raj")
st.sidebar.write("Powered by google gemini ai")
st.header("RoboBILL")
st.subheader("Made by DEV RAJ")
st.subheader("Manage Your expenses with RoboBILL")
input=st.text_input("What do you want me to do?",key="input")
uploaded_file = st.file_uploader("choose an image =",type=["jpg","jpeg","png"])
image=""
if uploaded_file is not None:
    image=Image.open(uploaded_file)
    st.image(image,caption="Uploaded Image",use_column_width=True)
    
ssubmit=st.button("LETS GO!")

input_prompt="""
You are an expert in reading invoices.
We are going to uploadan image of an 
invoice and you willhave to answer any
type of questions that the user asks you.
At the end,make sure to repeat the name of out app "RoboBILL"
and ask the user to use it again.
"""
if ssubmit:
    image_data=input_image_details(uploaded_file)
    response=get_gemini_response(input_prompt,image_data,input)
    st.subheader("Here's what you need to know!")
    st.write(response)


