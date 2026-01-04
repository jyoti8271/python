
import streamlit as st
import pandas as pd

st.title("streamlit text input")

name=st.text_input("enter your name:")
if name:
    st.write(f"hello,{name}")
    
    
data={
    "name":["john","jane","jake","jill"],
    "Age":[28,24,35,40],
    "city":["new york","los angeles","chicago","houston"]
}    
df=pd.DataFrame(data)
df.to_csv("sampledata.csv")
st.write(df)    
    
    
    
    ##slider
age = st.slider( "select your age:",0,100,25)     
st.write(f"your age is{age}.")

##selectbox

options=["python","java","c++","javascript"]
choice=st.selectbox("choose your favorite language:",options)
st.write(f"you selected {choice}.")



uploaded_files=st.file_uploader("choose a csv file",type='csv')

if uploaded_files is not None:
    df=pd.read_csv(uploaded_files)
    st.write(df)

