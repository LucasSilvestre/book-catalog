from typing import Tuple, Optional

from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError


class BasicModel:
    def update(self, db_session: Session, **kwargs) -> Tuple[bool, Optional[str]]:
        try:
            for (attribute, _) in self.__dict__.items():
                if kwargs.get(attribute):
                    setattr(self, attribute, kwargs.get(attribute))
            db_session.commit()
            return True, None
        except SQLAlchemyError as error:
            return False, " ".join(error.args)

    def save(self, db_session: Session) -> Tuple[bool, Optional[str]]:
        try:
            db_session.add(self)
            db_session.commit()
            return True, None
        except SQLAlchemyError as error:
            return False, " ".join(error.args)

    def remove(self, db_session: Session) -> Tuple[bool, Optional[str]]:
        try:
            db_session.delete(self)
            db_session.commit()
            return True, None
        except SQLAlchemyError as error:
            return False, " ".join(error.args)
