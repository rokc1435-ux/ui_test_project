import pytest

def test_admin_exists(user_db):
    assert "admin" in user_db
@pytest.mark.parametrize("username,age",[("admin",18),("guest",25)])
def test_user_age(user_db,username,age):
    assert user_db[username] == age

