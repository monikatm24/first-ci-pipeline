from app import add

def test_add():
    assert add(5, 3) == 9
    assert add(10, 20) == 30
    assert add(-5, 5) == 0
