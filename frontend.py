import streamlit as st 
import backend as backend

st.set_page_config(
                    page_title='QWERTY Typo Generator',
                    # page_icon="📈",#None,
                    layout="centered",
                    initial_sidebar_state="auto",
                    menu_items={'Report a Bug':'https://christiancardozo.com'},
                    )

st.title('Qwertypo generator')
st.write(backend.mess_text('It happens all too often.',0.3))
st.caption('© 20223 Christian Cardozo | http://christiancardozo.com')
st.text('version alpha 0.1: 09-30-2023')
st.write('')

col1, col2 = st.columns(2)
p_mistake = col1.slider('Error likelihood (%)',0,100,30)

col1, col2 = st.columns(2)
start_string = st.text_input('What are you trying to say?','The quick brown fox')
st.write('What you type:')
st.success(backend.mess_text(start_string,p_mistake/100))



