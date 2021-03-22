"""
Method for manipulating users in the database
"""

from typing import Union, Optional, List
from bson import ObjectId

from social_network.config import db
from ..models import User


def list_users() -> List[User]:
    return [User(**user) for user in db.users.find()]


def insert_user(user: User) -> User:
    existing_user = find_user_by_username(user.username)
    if existing_user is not None:
        return existing_user
    if hasattr(user, "user_id"):
        delattr(user, "user_id")
    response = db.users.insert_one(user.dict(by_alias=True))
    user.user_id = response.inserted_id
    return user


def find_user_by_id(user_id: Union[str, ObjectId]) -> Optional[User]:
    user = db.users.find_one({"_id": ObjectId(user_id)})
    if user is not None:
        user = User(**user)
    return user


def find_user_by_username(username: str) -> Optional[User]:
    user = db.users.find_one({"username": username})
    if user is not None:
        user = User(**user)
    return user


def delete_user(user_id: Union[str, ObjectId]) -> bool:
    result = db.users.delete_one({"_id": ObjectId(user_id)})
    return bool(result.deleted_count)
