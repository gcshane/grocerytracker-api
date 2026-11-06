from unittest.mock import MagicMock, patch

from fastapi.testclient import TestClient

from app.db.schema import User
from app.dependencies import get_session
from app.main import app
from app.services.auth_services import get_current_user

client = TestClient(app)


def test_get_lists_success():
    fake_user = User(
        user_id=1,
        username="testuser",
        name="Test User",
        email="test@example.com",
        password="hashed",
        alert=True,
    )
    mock_session = MagicMock()
    expected_response = {
        "lists": [
            {"list_id": 1, "list_name": "Weekly"},
            {"list_id": 2, "list_name": "Monthly"},
        ]
    }

    app.dependency_overrides[get_current_user] = lambda: fake_user
    app.dependency_overrides[get_session] = lambda: mock_session

    try:
        with patch("app.api.v1.lists_api.get_lists_service") as mock_get_lists_service:
            mock_get_lists_service.return_value = expected_response

            response = client.get("/lists")

            assert response.status_code == 200
            assert response.json() == expected_response
            mock_get_lists_service.assert_called_once_with(mock_session, fake_user)
    finally:
        app.dependency_overrides.clear()


def test_create_list_success():
    fake_user = User(
        user_id=1,
        username="testuser",
        name="Test User",
        email="test@example.com",
        password="hashed",
        alert=True,
    )
    mock_session = MagicMock()
    expected_response = {"list_id": 1, "list_name": "Weekly"}

    app.dependency_overrides[get_current_user] = lambda: fake_user
    app.dependency_overrides[get_session] = lambda: mock_session

    try:
        with patch("app.api.v1.lists_api.create_list_service") as mock_create_list_service:
            mock_create_list_service.return_value = expected_response

            response = client.post("/lists", json={"list_name": "Weekly"})

            assert response.status_code == 201
            assert response.json() == expected_response
            mock_create_list_service.assert_called_once_with(mock_session, "Weekly", fake_user)
    finally:
        app.dependency_overrides.clear()


def test_create_list_validation_error_when_list_name_missing():
    fake_user = User(
        user_id=1,
        username="testuser",
        name="Test User",
        email="test@example.com",
        password="hashed",
        alert=True,
    )
    mock_session = MagicMock()

    app.dependency_overrides[get_current_user] = lambda: fake_user
    app.dependency_overrides[get_session] = lambda: mock_session

    try:
        response = client.post("/lists", json={})

        assert response.status_code == 422
    finally:
        app.dependency_overrides.clear()
