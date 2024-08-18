from openai import AzureOpenAI
from env_EJEM import *
import streamlit as st

class GPT():
    def __init__(self) -> None:
        self.client = AzureOpenAI(api_version=AZURE_OPENAI_API_VERSION,api_key=AZURE_OPENAI_API_KEY,azure_endpoint=AZURE_OPENAI_ENDPOINT)
    
    def chat(self, system_prompt,request_prompt,stream=False):
        messages=[{'role':'system','content':system_prompt},{'role':'user','content':request_prompt}]
        try:
            response = self.client.chat.completions.create(model=AZURE_OPENAI_MODEL, messages=messages, stream=True)
            return response
            answer = response.choices[0].message.content
            return answer
        except Exception as e:
            st.error('Error en la petición a OpenAI: ', e)