import random

from .constants import *
import pytest
import constload


def test_value_is_set(instance):
    number = random.randint(1, 2000)
    instance._write_path(number, ("widget", "window", "name"))
    assert instance.data["widget"]["window"]["name"] == number


def test_zero_length_path(instance):
    instance._write_path({}, tuple())
    assert instance.data == {}


def test_bad_data_type(instance):
    with pytest.raises(TypeError):
        instance._write_path("hello", tuple())
