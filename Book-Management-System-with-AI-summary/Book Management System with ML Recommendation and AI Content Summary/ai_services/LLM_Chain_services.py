from pydantic import BaseModel, Field
from langchain.output_parsers import PydanticOutputParser
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain


from langchain_community.llms import Ollama
ollama = Ollama(base_url = 'http://localhost:11434', model = 'llama3')

##
# class WikiDataDim(BaseModel):
#     Summary : str = Field(...,description='the Summary of the given book content')

# WikidataDimParser = PydanticOutputParser(pydantic_object = WikiDataDim).get_format_instructions()


Book_Summary_Prompt_Template = '''You are a Book summarizer who get the data from Wikipedia API. And Summarize the book 
and give 100 - 150 word summary of the book content.

Check if the given Wikipedia data actually related to Books or not if not then clearly say you are here for Book Summarization only.

**If that's related book content. Dont Tell about the Wikipedia content just give summary no other words.

Book Content:
{wikipedia_data}
'''  

def get_prompt_template(wikipedia_data) -> PromptTemplate:
    Book_Summary_Prompt : PromptTemplate = PromptTemplate(
    template=Book_Summary_Prompt_Template,
    input_variables=[wikipedia_data],
    #partial_variables={'WikidataDimParser':WikidataDimParser}
    )   
    return Book_Summary_Prompt


def get_chain(Book_Summary_Prompt) -> LLMChain:
    chain : LLMChain = LLMChain(
    llm = ollama,
    prompt = Book_Summary_Prompt,
    verbose = True
    )
    return chain