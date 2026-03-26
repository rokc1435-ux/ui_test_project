import pytest

@pytest.fixture
def num():
    return 20
def test_bigger(num):
    assert num  > 10
def test_xx(num):
    assert num % 2 == 0

