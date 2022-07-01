from pydantic import BaseModel, Field
from typing import List, Union


class AuthorInfo(BaseModel):
    name: Union[str, None]
    birth_year: Union[int, None]
    death_year: Union[int, None]


class BookInfo(BaseModel):
    id: int
    title: str
    authors: List[AuthorInfo]
    languages: List[str]
    download_count: int


class BookInfoWithReview(BaseModel):
    id: int
    title: str
    authors: List[AuthorInfo]
    languages: List[str]
    download_count: int
    rating: float
    reviews: List[str]


class ListBookInfoWithReview(BaseModel):
    books: List[BookInfoWithReview]


class ListBooksInfo(BaseModel):
    books: List[BookInfo]


class ReviewBook(BaseModel):
    rvw_nr_book_id: int = Field(..., alias='bookId')
    rvw_nr_rating: float = Field(..., alias='rating', ge=0, le=5)
    rvw_tx_comment: str = Field(..., alias='review')


class BookNotFound(BaseModel):
    message: str = Field('Book not found.')


class NoReviewsFound(BaseModel):
    message: str = Field('No reviews found.')


class SuccessSavingReview(BaseModel):
    message: str


class ErrorSavingReview(BaseModel):
    message: str = Field('Error to save review.')
    details: str

class HTTPResponse(BaseModel):
    status: int
    body: Union[str, dict]
