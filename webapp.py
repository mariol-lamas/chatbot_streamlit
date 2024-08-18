import streamlit as st
from env_EJEM import *
import base64
import time
import os


class App():


    def __init__(self,gpt):
        self.gpt = gpt
        self.chat()
    
    def chat(self):
        st.markdown("""<h1 style="text-align: center;">Chatbot con Streamlit!</h1>""", unsafe_allow_html=True)
        col1,col2= st.columns([.95,.05])
        with col1:
            if st.button('Limpiar Chat'):
                st.session_state.messages = [{'role':'assistant','content':'¡Hola! ¿En que puedo ayudarte?'}]

        messages = st.container(height=500)

        if 'messages' not in st.session_state.keys():
            st.session_state.messages = [{'role':'assistant','content':'¡Hola! ¿En qué puedo ayudarte?'}]
        
        for message in st.session_state.messages:
            with messages.chat_message(message['role']):
                st.write(message['content'])
        
        col1_inf_v,col2_inf_v = st.columns([.95,.05])
        with col1_inf_v:
            prompt_d=st.chat_input(disabled=False,key='input_preg_doc_voice')

        if prompt_d:
            st.session_state.messages.append({'role':'user','content':prompt_d})
            with messages.chat_message('user'):
                st.write(prompt_d)
            
            if st.session_state.messages[-1]['role'] != 'assistant':
                with messages.chat_message('assistant'):
                    with st.spinner('Pensando...'):
                        try:
                            hist_mensajes = self.get_hist(2)
                            prompt= f'Tus respuesta anteriores {hist_mensajes}. Mi consulta: {prompt_d}.'
                            response = self.gpt.chat(SYSTEM_PROMPT,prompt)
                            st.write_stream(response)
                        except Exception as e:
                            print(e)
                            response = 'Parece que no te he entendido bien.'
                            st.write(response)
                mes = {'role':'assistant','content':response}
                st.session_state.messages.append(mes)
    
    def get_hist(self,n):

        if len(st.session_state.messages) < 2*n:
            n = round(len(st.session_state.messages)/2)
        
        interacciones=st.session_state.messages[-2*n:]

        historico="\n".join([f"{interaccion['role']}: {interaccion['content']}" for interaccion in interacciones if interaccion['role']=='assistant'])

        return historico
    
            