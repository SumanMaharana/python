import streamlit as st
import numpy as np
import pandas as pd
st.title("Suman Maharana")
st.write("MSc DSAI")
st.header("Python")
st.latex(r'''
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
    ''')
st.caption("Caption trial")
code = '''def hello():
    print("Hello, Streamlit Cloud!")'''
st.code(code, language='python')
df=pd.DataFrame(
   np.random.randn(10, 5),
   columns=('col %d' % i for i in range(5)))
st.table(df)
data=pd.DataFrame(
    np.random.randn(50,3),
    columns=['A','B','C']
)
st.line_chart(data)

col1,col2=st.columns(2)
with col1:
    st.header('Mountains')
    st.image("https://c4.wallpaperflare.com/wallpaper/658/800/994/simple-simple-background-minimalism-black-background-wallpaper-preview.jpg")

with col2:
    st.header('Itachi')
    st.image("https://c4.wallpaperflare.com/wallpaper/116/412/889/naruto-anime-uchiha-itachi-hd-wallpaper-preview.jpg")