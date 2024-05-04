from langchain_google_genai.llms import GoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory
import speech_recognition as sr
import base64
import streamlit as st
import gtts

def get_genai_llm(*,model_name:str, google_api_key:str, temperature:float, verbose:bool = True) -> GoogleGenerativeAI:
        return GoogleGenerativeAI(
                    model=model_name,
                    google_api_key=google_api_key,
                    temperature=temperature,
                    verbose=verbose
                )

template = """You are a nice chatbot having a conversation with a human. Your name is Amelia.
    The user going to ask aboout related to Indian Foods, Culture, States. So keep them engage, But also you have to check if the 
    conversation is happening on that context only or not. If not, Simply say in a very humble way that you are a chatbot who can
    discuss only related to India.
    
    Previous conversation:
    {chat_history}

    New human question: {question}
    Response:"""

def get_prompt_template(template : str) -> PromptTemplate:
      return PromptTemplate.from_template(template=template)



def get_llm_chain(llm, prompt_template : PromptTemplate, Conversationmemory, verbose:bool = True) -> LLMChain:

    chain = LLMChain(
        llm=llm,
        prompt=prompt_template,
        verbose=verbose,
        memory=Conversationmemory
    )
    return chain

def get_transcribe(audio_file_path):
    r = sr.Recognizer()
    audio = sr.AudioFile(f'./{audio_file_path}')
    with audio as source:
        audio = r.record(source)                  
        result = r.recognize_google(audio)
    return result

def autoplay_audio(file_path: str):
    with open(file_path, "rb") as f:
        data = f.read()
    b64 = base64.b64encode(data).decode("utf-8")
    md = f"""
    <audio autoplay>
    <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
    </audio>
    """
    st.markdown(md, unsafe_allow_html=True)

def text_to_speech(input_text):
     t1 = gtts.gTTS(input_text)
     webm_file_path = 'text-to-speech.mp3'
     with open(webm_file_path, 'wb'):
          t1.save(webm_file_path)
     return webm_file_path

