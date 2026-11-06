from sqlmodel import select

from app.db.schema import User
from app.dependencies import SessionDep


def get_user_by_username(username: str, session: SessionDep):
    user = session.exec(select(User).where(User.username == username)).first()
    return user

def get_user_by_email(email: str, session: SessionDep):
    user = session.exec(select(User).where(User.email == email)).first()
    return user

def get_user_by_id(user_id: int, session: SessionDep):
    user = session.exec(select(User).where(User.user_id == user_id)).first()
    return user

def create_new_user(user: User, session: SessionDep):
    session.add(user)
    session.commit()
    session.refresh(user)
    return user