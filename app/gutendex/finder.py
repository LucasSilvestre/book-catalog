import json

import requests

from sqlalchemy.orm import Session
from typing import Union
from fastapi.responses import JSONResponse

from app.settings import GUTENDEX_URL
from app.gutendex.schemas import (
    ListBooksInfo, BookInfoWithReview,
    BookNotFound, NoReviewsFound, HTTPResponse
)
from app.models.review import Review
from app.gutendex.utils import calculate_avage_rating, filter_every_comment
from app.services.cache import cache


class Finder:
    """
    Class to get book info.
    """
    def _get_book_info_by_title(self,
                                title: str) -> HTTPResponse:
        """
        Search book info for title at gutendex.

        :param title: Book title.
        :return: OBject HTTTPResponse with status code and body.
        """
        response = requests.get(f'{GUTENDEX_URL}/books?search={title}')
        return HTTPResponse(
            status=response.status_code,
            body=response.json()
        )

    def _get_book_info_by_id(self,
                             book_id: int) -> HTTPResponse:
        """
        Searcxh book info for id at gutendex.

        :param book_id: Book id.
        :return: OBject HTTTPResponse with status code and body.
        """
        response = requests.get(f'{GUTENDEX_URL}/books?ids={book_id}')
        return HTTPResponse(
            status=response.status_code,
            body=response.json()
        )

    def book_without_review(self,
                            title: str) -> Union[ListBooksInfo, JSONResponse]:
        """
        Get book info and format, not returning reviews done.

        :param title: Book title.
        :return: Object ListBooksInfo containing book information.
        """
        cached_value = cache.get_value(f'finder-without-review-{title}')
        if cached_value:
            cached_value = cached_value.decode('utf-8').replace("'", '"')
            cached_value = json.loads(cached_value)
            return ListBooksInfo(**cached_value)

        response = self._get_book_info_by_title(title)
        if not response.body['results']:
            return JSONResponse(
                content=dict(BookNotFound()),
                status_code=404
            )

        book_finder_anwser = ListBooksInfo(**({'books': response.body['results']}))
        cache.set_value(f'finder-without-review-{title}', str(book_finder_anwser.json()))
        return book_finder_anwser

    def book_with_review(self,
                         book_id: int,
                         db_session: Session) -> Union[BookInfoWithReview, JSONResponse]:
        """
        Get book info and format with all reviews done.

        :param book_id: Book id.
        :param db_session: Database connection.
        :return: Object BookInfoWithReview containing book information and reviews.
        """
        cached_value = cache.get_value(f'finder-with-review-{book_id}')
        if cached_value:
            cached_value = cached_value.decode('utf-8').replace("'", '"')
            cached_value = json.loads(cached_value)
            return BookInfoWithReview(**cached_value)

        response = self._get_book_info_by_id(book_id)
        results = response.body['results']
        if not results:
            return JSONResponse(
                content=dict(BookNotFound()),
                status_code=404
            )
        book_search = response.body['results'][0]

        all_reviews = Review().get_by_book_id(book_id, db_session)
        if not all_reviews:
            return JSONResponse(
                content=dict(NoReviewsFound()),
                status_code=404
            )

        book_search['rating'] = calculate_avage_rating(all_reviews)
        book_search['reviews'] = filter_every_comment(all_reviews)

        book_finder_with_anwser = BookInfoWithReview(**book_search)
        cache.set_value(f'finder-with-review-{book_id}', str(book_finder_with_anwser.json()))

        return BookInfoWithReview(**book_search)
