import streamlit as st
from gpt import GPT
from webapp import App
from env_EJEM import *
import asyncio
st.set_page_config(layout='wide',initial_sidebar_state='collapsed')

async def start():
    gpt = GPT()
    app= App(gpt=gpt)

if __name__=='__main__':
    asyncio.run(start())
