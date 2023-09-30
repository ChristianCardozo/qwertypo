import streamlit as st 
import backend as backend

st.set_page_config(
                    page_title='QWERTY Typo Generator',
                    # page_icon="📈",#None,
                    layout="centered",
                    initial_sidebar_state="auto",
                    # menu_items={'Report a Bug':'https://christiancardozo.com'},
                    )

# col1, col2, col3 = st.columns(3)
st.title('Qwertypo')
st.write(backend.mess_text('Exploring an element of the modern human condition.'))
st.caption('© 2023 Christian Cardozo | http://christiancardozo.com')
# st.text('version alpha 0.1: 09-30-2023')

# col1, col2, col3 = st.columns(3)
p_mistake = st.slider('Typo likelihood (%)',0,100,20)

# col1, col2, col3 = st.columns(3)
start_string = st.text_input('What are you trying to say?','The quick brown fox')
st.write('What you ultimately type:')
st.success(backend.mess_text(start_string,p_mistake/100))



