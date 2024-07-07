from pydantic import BaseModel, Field

class Book(BaseModel):
    title : str = Field(description='The title of the Book')
    author : str = Field(description='The author who written the book')
    genre : str = Field(description='the category or style of a book')
    year_published: int = Field(description='The year when the book published')
    summary: str = Field(description='Casual Summary of the written book')
