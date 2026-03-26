import pytest
@pytest.fixture(scope="session")
def user_db():
    print("\n连接数据库")
    yield {"admin": 18,"guest":25}
    print("\n清理用户数据库")
    