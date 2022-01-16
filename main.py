from multiprocessing import Condition
from tkinter.ttk import Style
import streamlit as st
from PIL import Image

st.title("超入門")

st.write("Image")
if st.checkbox("show image"):
  img = Image.open("sample.jpg")
  st.image(img, caption="japan", use_column_width=True)

condition = st.sidebar.slider("あなたの今の調子は？", 0, 100, 50)
text = st.sidebar.text_input("あなたの趣味を教えてください")
st.write("あなたの趣味は",text,"です")
st.write("あなたのコンディションは",condition,"です")
