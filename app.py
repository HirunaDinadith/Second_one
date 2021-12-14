import streamlit as st

options = ['Hello', 'World']
st.sidebar.selectbox('Options', options)
st.title('Hello World')
st.write('This is my second web hosted application')

video_file = open('How the COVID-19 virus is transmitted 1080 x 1920.mp4','rb')
video_bytes = video_file.read()

st.video(video_bytes)
