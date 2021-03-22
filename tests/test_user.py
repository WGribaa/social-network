from social_network.db.users import *
from social_network.models import User

user_test = {"username": "splash"}


def test_insert_user():
    user = insert_user(User(**user_test))
    assert isinstance(user, User)
    assert hasattr(user, "user_id")
    assert user == User(**user_test)


def test_list_user():
    users = list_users()
    assert len(users) == 1
    assert users[0] == User(**user_test)


def test_insert_existing_user():
    _ = insert_user(User(**user_test))
    assert len(list_users()) == 1


def test_find_user_by_id():
    user = insert_user(User(**user_test))
    db_user = find_user_by_id(user.user_id)
    assert db_user is not None
    assert db_user == user


def test_find_user_by_username():
    user = insert_user(User(**user_test))
    db_user = find_user_by_username(user.username)
    assert db_user is not None
    assert db_user == user

def test_delete_user():
    user = insert_user(User(**user_test))
    response = delete_user(user.user_id)
    assert response == True
    assert len(list_users()) == 0

def test_delete_non_existing_user():
    response = delete_user("123456781234567812345678")
    assert response == False
