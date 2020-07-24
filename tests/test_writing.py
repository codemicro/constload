import random

from .constants import *
import pytest
import constload


def test_value_is_set(instance):
    number = random.randint(1, 2000)
    instance._write_path(number, "widget", "window", "name")
    assert instance.data["widget"]["window"]["name"] == number
