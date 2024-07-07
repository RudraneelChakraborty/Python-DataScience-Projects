import uvicorn
from fastapi import FastAPI,  HTTPException
from fastapi.middleware.cors import CORSMiddleware
from routers import books_router,book_recommendation_router,llm_router

import sys
sys.dont_write_bytecode = True

app = FastAPI()

app.include_router(books_router.router)
app.include_router(book_recommendation_router.router)
app.include_router(llm_router.router)

#Configure for security
app.add_middleware(
    CORSMiddleware,
    # allow_origin = ["*"],
    # allow_credentials = True,
    allow_methods = ["*"] , 
    allow_headers = ["*"]
)

@app.get('/')
async def root():
    return {'status':'Application is running'}

@app.get('/health_check')
async def health_check():
    try:
        return {'status':'Healthy'}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0',port = 8001, reload=True)