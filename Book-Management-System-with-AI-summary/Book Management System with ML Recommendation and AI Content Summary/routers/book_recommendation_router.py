import pickle
from fastapi import APIRouter, HTTPException
from fuzzywuzzy import fuzz, process
import sklearn
import pandas as pd


router = APIRouter(
    prefix='/recommendations',
    tags=['Books Recommendation']
)

with open('././ML_Recommendation/Book_List.pkl', 'rb') as f:
    Book_List = pickle.load(f)

with open('././ML_Recommendation/NearestNeighbors_model.pkl', 'rb') as f:
    model_knn = pickle.load(f)

# with open('././ML_Recommendation/User_rating_pivot.pkl', 'rb') as f:
#     user_rating_pivot = pickle.load(f)
user_rating_pivot = pd.read_pickle('././ML_Recommendation/User_rating_pivot.pkl')



@router.get('/')
def get_recommendation(book_name : str):
    match = process.extractBests(book_name, Book_List, limit=1)
    query_index = user_rating_pivot.index.get_loc(match[0][0])
    distances, indices = model_knn.kneighbors(user_rating_pivot.iloc[query_index,:].values.reshape(1, -1), n_neighbors = 6)
    recommendation_list = []
    for i in range(0, len(distances.flatten())):
        if i == 0:
            print(f'Recommendations for {book_name}')
        else:
            print('{0}: {1}, with distance of {2}:'.format(i, user_rating_pivot.index[indices.flatten()[i]], distances.flatten()[i]))
            recommendation_list.append(user_rating_pivot.index[indices.flatten()[i]])

    return recommendation_list

