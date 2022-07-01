from unittest.mock import patch

from app.gutendex.finder import Finder
from app.services.cache import Cache
from app.models.review import Review


def test_book_finder_without_rating(web_client,
                                    find_book,
                                    sucess_find_book):
    """
    Test find book by his title.
    """
    with patch.object(Cache, 'set_value', return_value=True):
        with patch.object(Cache, 'get_value', return_value=None):
            with patch.object(Finder, '_get_book_info_by_title', return_value=find_book):
                result = web_client.get(f'/book/Frankenstein; Or, The Modern Prometheus')
    assert result.status_code == 200
    assert result.json() == sucess_find_book


def test_book_finder_with_book_not_found(web_client,
                                         book_not_found,
                                         book_not_found_response):
    """
    Test book not found cenary.
    """
    with patch.object(Cache, 'set_value', return_value=True):
        with patch.object(Cache, 'get_value', return_value=None):
            with patch.object(Finder, '_get_book_info_by_title', return_value=book_not_found):
                result = web_client.get(f'/book/mock-request')
    assert result.status_code == 404
    assert result.json() == book_not_found_response


def test_post_book_review(web_client,
                          db_client,
                          post_book_review):
    """
    Post a review to a book.
    """
    first_review = Review.get_by_book_id(post_book_review['bookId'], db_client)
    assert not first_review
    response = web_client.post(f'/book/review', json=post_book_review)
    first_review = Review.get_by_book_id(post_book_review['bookId'], db_client)
    assert response.json() == {"message": "Success saving review."}
    assert len(first_review) == 1


def test_get_book_review(web_client,
                         find_book,
                         db_client,
                         post_book_review):
    """
    Test get a book review.
    """
    web_client.post(f'/book/review', json=post_book_review)
    post_book_review['rating'] = 5
    web_client.post(f'/book/review', json=post_book_review)
    with patch.object(Cache, 'set_value', return_value=True):
        with patch.object(Cache, 'get_value', return_value=None):
            with patch.object(Finder, '_get_book_info_by_id', return_value=find_book):
                result = web_client.get(f'/book/review/84')
    assert result.status_code == 200
    assert result.json()['rating'] == 4.0
    assert len(result.json()['reviews']) == 2


def test_get_book_review_with_book_not_found(web_client,
                                             book_not_found,
                                             book_not_found_response):
    """
    Test get a book review, but book doesn't exists.
    """
    with patch.object(Cache, 'set_value', return_value=True):
        with patch.object(Cache, 'get_value', return_value=None):
            with patch.object(Finder, '_get_book_info_by_id', return_value=book_not_found):
                result = web_client.get(f'/book/review/84')

    assert result.status_code == 404
    assert result.json() == book_not_found_response


def test_get_book_review_with_no_book_reviews(web_client,
                                              db_client,
                                              find_book):
    """
     Test get a book review, but review doesn't exists.
    """
    with patch.object(Cache, 'set_value', return_value=True):
        with patch.object(Cache, 'get_value', return_value=None):
            with patch.object(Finder, '_get_book_info_by_id', return_value=find_book):
                result = web_client.get(f'/book/review/84')

    assert result.status_code == 404
    assert result.json() == {'message': 'No reviews found.'}


def test_get_top_ratting_books(web_client,
                               db_client,
                               post_book_review,
                               success_top_rating):
    """
    Get top ratting books.
    """
    # Do 2 reviews for book 84
    web_client.post(f'/book/review', json=post_book_review)
    post_book_review['rating'] = 5
    web_client.post(f'/book/review', json=post_book_review)
    # Do 2 reviews for book 83
    post_book_review['bookId'] = 83
    post_book_review['rating'] = 2
    web_client.post(f'/book/review', json=post_book_review)
    post_book_review['bookId'] = 83
    post_book_review['rating'] = 3
    web_client.post(f'/book/review', json=post_book_review)
    # Do 2 reviews for book 82
    post_book_review['bookId'] = 82
    post_book_review['rating'] = 1
    web_client.post(f'/book/review', json=post_book_review)
    post_book_review['bookId'] = 82
    post_book_review['rating'] = 2
    web_client.post(f'/book/review', json=post_book_review)
    with patch.object(Cache, 'set_value', return_value=True):
        with patch.object(Cache, 'get_value', return_value=None):
            result = web_client.get(f'/book/top_rating/3')

    assert result.json() == success_top_rating
    assert result.status_code == 200



