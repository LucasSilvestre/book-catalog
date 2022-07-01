from typing import Union
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse

from app.models.review import Review as ReviewModel
from app.gutendex.finder import Finder
from app.gutendex.schemas import ReviewBook, ErrorSavingReview, SuccessSavingReview, ListBookInfoWithReview


class Review:
    def save_book(self,
                  review: ReviewBook,
                  db_session: Session) -> Union[SuccessSavingReview,
                                                JSONResponse]:
        """
        Save book review at our database.

        :param review: Information with Book ID and the Review Done.
        :param db_session: Database connection.
        :return: Message with Success.
        """
        try:
            review = ReviewModel(**review.dict())
            review.save(db_session)
            return SuccessSavingReview(message="Success saving review.")
        except Exception as err:
            return JSONResponse(
                content=ErrorSavingReview(details=err),
                status_code=500
            )

    def top_book(self,
                 top: int,
                 db_session: Session):
        """
        Get Top rating book.

        :param top: Number of top books to filter.
        :param db_session: Database connection.
        :return: List of books order by rating.
        """
        top_avarage = ReviewModel().get_top_avarage(top, db_session)
        list_of_books = list()
        for book_id, _ in top_avarage:
            list_of_books.append(Finder().book_with_review(book_id, db_session))
        return ListBookInfoWithReview(**{'books': list_of_books})
