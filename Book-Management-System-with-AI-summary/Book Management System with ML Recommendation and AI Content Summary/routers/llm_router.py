from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from ai_services import LLM_Chain_services, WikiBookRunner
from typing import Optional

router = APIRouter(
    prefix='/generate-summary',
    tags=['LLM Services']
)

@router.post('/')
def get_summary_from_book_content(Book_Name : Optional[str] = '', Book_Content : Optional[str] = ''):
    if Book_Name != '':
        WikiContent = WikiBookRunner.get_Wiki_Content(Book_Name)
        Book_Prompt = LLM_Chain_services.get_prompt_template(WikiContent)
        book_chain = LLM_Chain_services.get_chain(Book_Prompt)
        return_data = book_chain.invoke(input=WikiContent)
        return JSONResponse(content=return_data['text'])
    
    if Book_Content != '' and len(Book_Content) > 30 :
        Book_Prompt = LLM_Chain_services.get_prompt_template(Book_Content)
        book_chain = LLM_Chain_services.get_chain(Book_Prompt)
        return_data = book_chain.invoke(input=Book_Content)
        return JSONResponse(content=return_data['text'])
    
    if Book_Name == '' and len(Book_Content) < 20:
        return {'message' : 'Not enough content summaries'}
    