from .constants import *
import pytest
import constload

"""
To test the ConstantLoader._resolve_path function
"""


def test_existing_path(instance):
    print(sample_data["widget"]["window"]["height"], instance._resolve_path("widget", "window", "height"))
    assert instance._resolve_path("widget", "window", "height") == sample_data["widget"]["window"]["height"]
    assert instance._resolve_path("widget") == sample_data["widget"]


def test_nonexistent_path(instance):
    with pytest.raises(KeyError):
        instance._resolve_path("this", "should", "not", "exist")


def test_empty_path(instance):
    assert instance._resolve_path() == sample_data
