from sqlmodel import select

from app.dependencies import SessionDep
from app.db.schema import User, List


def get_lists_service(session: SessionDep, current_user: User):
    lists = session.exec(select(List).where(List.user_id == current_user.user_id)).all()
    return {
        "lists": [
            {"list_id": grocery_list.list_id, "list_name": grocery_list.list_name}
            for grocery_list in lists
        ]
    }


def create_list_service(session: SessionDep, list_name: str, current_user: User):
    new_list = List(list_name=list_name, user_id=current_user.user_id)
    session.add(new_list)
    session.commit()
    session.refresh(new_list)
    return {
        "message": "List created successfully.",
        "list": {"list_id": new_list.list_id, "list_name": new_list.list_name},
    }