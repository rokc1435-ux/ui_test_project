import pytest
@pytest.mark.parametrize("add_num,expected",[
    (1,11),
    (2,12),
    (3,13),
])
def test_add_base(base,add_num,expected): 
    assert base + add_num == expected