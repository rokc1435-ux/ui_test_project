import pytest
@pytest.fixture(scope = "session")
def data_a():
    return 1
@pytest.fixture(scope = "session")
def my_file():
    print("\n连接数据库")
    yield "db_connection"
    print("\n断开数据库")
def test_one(my_file):
    assert my_file == "db_connection"
def test_two(my_file):
    assert my_file == "db_connection"

