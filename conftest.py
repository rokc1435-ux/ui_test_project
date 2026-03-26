import pytest
from selenium import webdriver
@pytest.fixture(scope="session")
def db():
    print("\n连接数据库")
    yield "db_connection"
    print("\n断开数据库")
@pytest.fixture
def base():
    return 10
@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
    
