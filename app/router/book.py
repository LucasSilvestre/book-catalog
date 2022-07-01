from fastapi import APIRouter, Depends, Path
from typing import Union

from app.gutendex.finder import Finder
from app.gutendex.review import Review
from app.gutendex.schemas import (
    ListBooksInfo, ReviewBook, BookNotFound,
    SuccessSavingReview, ErrorSavingReview
)
from app.services.database import get_conn, Session

router = APIRouter()


@router.get('/{book_title}',
            status_code=200,
            response_model=Union[ListBooksInfo,
                                 BookNotFound],
            description="Search for a book info")
async def get_book_information(book_title: str):
    """
    Return information about the requested title.

    :param book_title: Tittle of book to be searched.
    :return: Info about the book title.
    """
    return Finder().book_without_review(book_title)


@router.post('/review',
             status_code=200,
             response_model=Union[SuccessSavingReview,
                                  ErrorSavingReview],
             description="Write a review for a book")
async def review_a_book(review: ReviewBook,
                        db_session: Session = Depends(get_conn)):
    """
    Post a review to a book identified by his ID.

    :param review: ReviewBook Object containing a review.
    :param db_session: Database connection.
    :return: Status of the posted review.
    """
    return Review().save_book(review, db_session)


@router.get('/review/{book_id}/',
            status_code=200,
            description="Get reviews from a book")
async def get_book_review(book_id: int = Path(title='Book id', gt=0, default=None),
                          db_session: Session = Depends(get_conn)):
    """
    Get information from a book with his reviews.

    :param book_id: Book identification at gutendex.
    :param db_session: Database connection.
    :return: Information about the book and his reviews.
    """
    return Finder().book_with_review(book_id, db_session)


@router.get('/top_rating/{top}',
            status_code=200,
            description="Return the top reviewed books")
async def get_top_reviewed_book(top: int = Path(title='Number of top books to get', gt=0, default=None),
                                db_session: Session = Depends(get_conn)):
    """
    Return the top N books based on their avarage rating.

    :param book_id: Book identification at gutendex.
    :param db_session: Database connection.
    :return: Top Books searched.
    """
    return Review().top_book(top, db_session)
