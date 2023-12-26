
from bank import value

def test_value():
    assert value("hello, world") == 0
    assert value("how are you") == 20
    assert value("table") == 100
    assert value("Hello World") == 0
    assert value("How are you") == 20
