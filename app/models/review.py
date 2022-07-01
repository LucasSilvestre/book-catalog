from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.orm import Session
from sqlalchemy.sql import func

from app.models import BasicModel
from app.services.database import BaseModel


class Review(BasicModel, BaseModel):
    __tablename__ = 'review'
    rvw_pk_review = Column(Integer, primary_key=True, autoincrement=True)
    rvw_nr_book_id = Column(Integer, nullable=False)
    rvw_nr_rating = Column(Float, nullable=False)
    rvw_tx_comment = Column(String(1000), nullable=False)
    rvw_dt_creation = Column(DateTime, nullable=False, server_default="NOW()")

    @classmethod
    def get_by_book_id(cls,
                       book_id: int,
                       db_session: Session):
        return db_session.query(cls).filter_by(rvw_nr_book_id=book_id).all()


    @classmethod
    def get_top_avarage(cls,
                        top: int,
                        db_session: Session):
        return db_session.query(
            cls.rvw_nr_book_id,
            func.avg(cls.rvw_nr_rating).label('average_rating')
        ).group_by(cls.rvw_nr_book_id) \
            .order_by(func.avg(cls.rvw_nr_rating).desc()).limit(top).all()
