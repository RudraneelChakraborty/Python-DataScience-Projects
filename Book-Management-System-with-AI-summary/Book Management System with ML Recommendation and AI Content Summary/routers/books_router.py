from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from connections import oracledb_con
from datamodels.Books import Book
from datamodels.Review import Review
import oracledb


router = APIRouter(
    prefix='/books',
    tags=['Books Management System']
)




@router.get('/')
async def retrive_books():
    try:
        conn = oracledb_con.oracle_get_conn()
        cursor = conn.cursor()
        cursor.execute('select * from books')
        books = cursor.fetchall()
        book_dict = {}
        for book in books:
            book_list = [book[1], book[2], book[3], book[4], book[5].read()]
            book_dict[book[0]] = book_list  
        return (book_dict)
    except Exception as e:
        raise e

@router.post('/')
def add_book(book: Book):
    conn = oracledb_con.oracle_get_conn()
    curser = conn.cursor()
    curser.execute(
        'INSERT into books (ID,TITLE,AUTHOR,GENRE,YEAR_PUBLISHED,SUMMARY) values (null,:1,:2,:3,:4,:5)',
        (book.title,book.author,book.genre,book.year_published,book.summary)
    )
    conn.commit()
    curser.close()
    return {'message':f'{book.title} has been added successfully'}

@router.get('/{id}')
def get_book_by_id(id : int):
    try:
        curser = oracledb_con.oracle_get_conn().cursor()
        curser.execute('Select * from books where id = :1', (id,))
        book = curser.fetchone()
        curser.close()
        if not book:
            raise HTTPException(status_code=404,detail='Book not found')
        book_list = [book[1], book[2], book[3], book[4], book[5].read()]
        return book_list
    except Exception as e:
        raise e
    
@router.put('/{id}')
def update_book_info(id:int,book:Book):
    conn = oracledb_con.oracle_get_conn()
    curser = conn.cursor()
    curser.execute(
        'update books set TITLE = :1,AUTHOR = :2,GENRE = :3,YEAR_PUBLISHED = :4,SUMMARY = :5 where id = :6',
        (book.title,book.author,book.genre,book.year_published,book.summary, id)
    )
    conn.commit()
    curser.close()
    return {'message' : 'Book updated'}

@router.delete('/{id}')
def delete_book_by_id(id:int):
    conn = oracledb_con.oracle_get_conn()
    curser = conn.cursor()
    curser.execute(
        'delete from reviews where book_id = :1',(id,)
        )
    curser.execute(
        'delete from books where id = :1',(id,)
        )
    conn.commit()
    curser.close()
    return {'message':'Book Deleted'}

@router.post('/{id}/reviews')
def add_review(id: int, review : Review):
    conn = oracledb_con.oracle_get_conn()
    curser = conn.cursor()
    curser.execute(
        'InSert into reviews values(null,:1,:2,:3,:4)',
        (id,review.user_id,review.review_text,review.rating)
    )
    conn.commit()
    curser.close()
    return {'message':'Review added successfully'}

@router.get('/{id}/reviews')
def get_review(id:int):
    conn = oracledb_con.oracle_get_conn()
    curser = conn.cursor()
    curser.execute('Select * from reviews where book_id = :1', (id,))
    reviews = curser.fetchall()
    review_dict = {}
    for review in reviews:
        review_list = [review[1], review[2], review[3].read(), review[4]]
        review_dict[review[0]] = review_list  
    return (review_dict)
