from typing import List
from app.models.review import Review


def calculate_avage_rating(reviews: List[Review]) -> float:
    """
    Calculate avarage rating of a list of reviews.
    :param reviews: List of Reviews.
    :return: Float number with the avarege rating.
    """
    return round(sum(review.rvw_nr_rating for review in reviews) / len(reviews), 2)


def filter_every_comment(reviews: List[Review]) -> List[str]:
    """
    Filter comments in a list of reviews.
    :param reviews: List of reviews.
    :return: Return a list with all the comments.
    """
    return list(review.rvw_tx_comment for review in reviews)
