# AI Voice Assistant for Context Aware Discussion

This is a Chatbot app created with Langchain, Streamlit, Google Gemini.

I make the Prompt Template to discuss on Indian food and culture, Anyone can change and the chatbot will discuss on that topic only.

It uses Speech To Text and Text-to-Speech to get the prompt from user and say the response.

In the ChatApp some can type along with someone can use by giving voice prompt. For both the cases AI Assistant will give back response in text along with it will say in a Voice.

# Steps to run 
* pip install -r requirements.txt
* streamlit run app.py

# Notes 
*  As, this is going to run in streamlit sometime the UI might break, Later on I will create a React App to make adjustments. But the skeliton will help anyone if somebody wanted to build Context Aware AI Voice Assistant with memory for better conversation experience.
*  Right now, I haven't handled any exception, So sometime it might show issues while creating audio files or reading audio files, Anytime that happen delete the file
 from directory and rerun the app.
