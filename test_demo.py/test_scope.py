import pytest
@pytest.fixture(scope="function")
def data_a():
    print("\n准备data_a")
    return 1

@pytest.fixture(scope="session")
def data_b():
    print("\n准备data_b")
    return 2
@pytest.fixture(scope="session")
def my_file():
    print("\n打开文件")
    yield "文件内容"
    print("\n关闭文件")

def test_read(my_file):
    assert my_file == "文件内容"
def test_one(data_a,data_b):
    result = 1
    assert result == 1
def test_two(data_b,data_a):
    result = 2
    assert result == 2
