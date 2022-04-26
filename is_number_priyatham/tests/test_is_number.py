from datetime import datetime

from is_number_priyatham import is_number
from is_number_priyatham import is_float


def test_is_number():
    assert is_number(1)


def test_is_not_number():
    assert not is_number("Hello world")
    assert not is_number({"Hello": "world"})
    assert not is_number(datetime.now())
    assert not is_number(lambda foo: foo)

def test_is_float():
    assert is_float(1.1)

    assert not is_float(1)
    assert not is_float(1.0)
    assert not is_float("Hello world")
    assert not is_float({"Hello": "world"})
    assert not is_float(datetime.now())
    assert not is_float(lambda foo: foo)