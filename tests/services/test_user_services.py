from unittest.mock import patch
from sqlmodel import create_engine, Session

from app.db.database import init_db
from app.db.schema import User
from app.services.user_services import get_user_by_username, get_user_by_id, create_new_user

def test_get_user_by_username_successful():
    test_engine = create_engine("sqlite:///:memory:")

    with patch("app.db.database.engine", test_engine):

        init_db()

        with Session(test_engine) as session:
            fake_user = User(
                user_id=1,
                username="test_sqlite_user", 
                name="Test", 
                email="test@test.com", 
                password="hashed", 
                alert=True
            )
            session.add(fake_user)
            session.commit()

            assert get_user_by_username("test_sqlite_user", session) == fake_user

def test_get_non_existent_user_by_username():
    test_engine = create_engine("sqlite:///:memory:")

    with patch("app.db.database.engine", test_engine):

        init_db()

        with Session(test_engine) as session:
            fake_user = User(
                user_id=1,
                username="test_sqlite_user", 
                name="Test", 
                email="test@test.com", 
                password="hashed", 
                alert=True
            )

            session.add(fake_user)
            session.commit()

            assert get_user_by_username("non_existent_user", session) is None

def test_get_user_by_id_successful():
    test_engine = create_engine("sqlite:///:memory:")

    with patch("app.db.database.engine", test_engine):

        init_db()

        with Session(test_engine) as session:
            fake_user = User(
                user_id=1,
                username="test_sqlite_user", 
                name="Test", 
                email="test@test.com", 
                password="hashed", 
                alert=True
            )
            session.add(fake_user)
            session.commit()

            assert get_user_by_id(1, session) == fake_user

def test_get_non_existent_user_by_id():
    test_engine = create_engine("sqlite:///:memory:")

    with patch("app.db.database.engine", test_engine):

        init_db()

        with Session(test_engine) as session:
            fake_user = User(
                user_id=1,
                username="test_sqlite_user", 
                name="Test", 
                email="test@test.com", 
                password="hashed", 
                alert=True
            )

            session.add(fake_user)
            session.commit()

            assert get_user_by_id(2, session) is None
    
def test_create_new_user_success():
    test_engine = create_engine("sqlite:///:memory:")

    with patch("app.db.database.engine", test_engine):

        init_db()

        with Session(test_engine) as session:
            fake_user = User(
                username="test_sqlite_user", 
                name="Test", 
                email="test@test.com", 
                password="hashed", 
                alert=True
            )
            result = create_new_user(fake_user, session)
            assert result.username == "test_sqlite_user"
            assert result.user_id is not None