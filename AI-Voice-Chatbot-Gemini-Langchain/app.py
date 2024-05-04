import streamlit as st 
from langchain_google_genai import GoogleGenerativeAI
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory
from audio_recorder_streamlit import audio_recorder
from langchain.prompts import PromptTemplate
from streamlit_float import *
from dotenv import load_dotenv

from dataclasses import dataclass
import os
from dataclasses import dataclass
import utils

load_dotenv()
float_init()

@dataclass
class Message:
    actor:str
    payload:str 

USER = "user"
ASSISTANT = "ai"
MESSAGES = "messages"

llm = utils.get_genai_llm(model_name='models/gemini-pro', google_api_key=os.getenv('GOOGLE_AI_API_TOKEN'),temperature=0.7)
prompt_template = utils.get_prompt_template(utils.template)
memory = ConversationBufferMemory(memory_key="chat_history")

def initialize_session_state():
    if MESSAGES not in st.session_state:
        st.session_state[MESSAGES] = [Message(actor=ASSISTANT, payload="Hi! How can I help you?😊")]
    if "llm_chain" not in st.session_state:
        st.session_state["llm_chain"] = utils.get_llm_chain(llm=llm,prompt_template=prompt_template,Conversationmemory=memory)

def get_llm_chain_from_session() -> LLMChain:
    return st.session_state["llm_chain"]

initialize_session_state()


msg: Message
for msg in st.session_state[MESSAGES]:
    st.chat_message(msg.actor).write(msg.payload)

prompt: str = st.chat_input("Enter a prompt here")

if prompt:
    st.session_state['audio_recorded'] = False
    st.session_state[MESSAGES].append(Message(actor=USER, payload=prompt))
    st.chat_message(USER).write(prompt)
    
    with st.spinner("Please wait.."):
        llm_chain = get_llm_chain_from_session()
        response: str = llm_chain({"question": prompt})["text"]
        st.session_state[MESSAGES].append(Message(actor=ASSISTANT, payload=response))
        st.chat_message(ASSISTANT).write(response)

    with st.spinner('Creating Audio Transcribe..'):
        audio = utils.text_to_speech(response)
        utils.autoplay_audio(audio)

st.session_state['audio_recorded'] = False
#audio_recorded = False

footer_container = st.container()
with footer_container:
    audio_bytes = audio_recorder()

    if audio_bytes:
        st.session_state['audio_recorded']  = True

if st.session_state['audio_recorded'] :
    with st.spinner('Transcribing..'):
        webm_file_path = 'temp-audio.mp3'
        with open(webm_file_path,'wb') as f:
            f.write(audio_bytes)
        
        transcript = utils.get_transcribe(webm_file_path)
        os.remove(webm_file_path)

    st.session_state['audio_recorded'] = False

    with st.spinner('Please Wait..'):
        if transcript:
            st.session_state[MESSAGES].append(Message(actor=USER, payload=transcript))
            st.chat_message(USER).write(transcript)
            llm_chain = get_llm_chain_from_session()
            response: str = llm_chain({"question": transcript})["text"]
            st.session_state[MESSAGES].append(Message(actor=ASSISTANT, payload=response))
            st.chat_message(ASSISTANT).write(response)
    del audio_bytes

    st.write(response)
    with st.spinner('Creating Audio Transcribe..'):
        audio = utils.text_to_speech(response)
        utils.autoplay_audio(audio)

footer_container.float("bottom: 0rem;")