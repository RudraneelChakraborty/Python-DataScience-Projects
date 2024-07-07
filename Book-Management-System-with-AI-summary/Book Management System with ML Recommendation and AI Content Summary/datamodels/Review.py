from pydantic import BaseModel, Field

class Review(BaseModel):
    user_id: str = Field(description='The ID of the User who gave the rating')
    review_text: str = Field(description='The Review given the User')
    rating: int = Field(description='The rating which is given by the user')