from unittest.mock import patch

from sqlmodel import Session, create_engine, select

from app.db.database import init_db
from app.db.schema import List, User
from app.services.list_services import create_list_service, get_lists_service


def test_get_lists_service_returns_only_current_user_lists():
    test_engine = create_engine("sqlite:///:memory:")

    with patch("app.db.database.engine", test_engine):
        init_db()

        with Session(test_engine) as session:
            user_one = User(
                username="user_one",
                name="User One",
                email="one@test.com",
                password="hashed",
                alert=True,
            )
            user_two = User(
                username="user_two",
                name="User Two",
                email="two@test.com",
                password="hashed",
                alert=True,
            )
            session.add(user_one)
            session.add(user_two)
            session.commit()
            session.refresh(user_one)
            session.refresh(user_two)

            session.add(List(list_name="Weekly", user_id=user_one.user_id))
            session.add(List(list_name="Monthly", user_id=user_one.user_id))
            session.add(List(list_name="Other User List", user_id=user_two.user_id))
            session.commit()

            result = get_lists_service(session, user_one)

            assert "lists" in result
            assert len(result["lists"]) == 2
            assert {item["list_name"] for item in result["lists"]} == {"Weekly", "Monthly"}


def test_get_lists_service_returns_empty_when_no_lists_exist():
    test_engine = create_engine("sqlite:///:memory:")

    with patch("app.db.database.engine", test_engine):
        init_db()

        with Session(test_engine) as session:
            user = User(
                username="no_lists_user",
                name="No Lists",
                email="nolists@test.com",
                password="hashed",
                alert=True,
            )
            session.add(user)
            session.commit()
            session.refresh(user)

            result = get_lists_service(session, user)

            assert result == {"lists": []}


def test_create_list_service_success():
    test_engine = create_engine("sqlite:///:memory:")

    with patch("app.db.database.engine", test_engine):
        init_db()

        with Session(test_engine) as session:
            user = User(
                username="creator",
                name="Creator",
                email="creator@test.com",
                password="hashed",
                alert=True,
            )
            session.add(user)
            session.commit()
            session.refresh(user)

            result = create_list_service(session, "Weekly", user)

            saved_list = session.exec(
                select(List).where(
                    List.list_name == "Weekly", List.user_id == user.user_id
                )
            ).first()

            assert result["list_name"] == "Weekly"
            assert result["list_id"] is not None
            assert saved_list is not None
            assert saved_list.user_id == user.user_id
