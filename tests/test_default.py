from .constants import *
import pytest
import constload

"""
To test the ConstLoader.pick_default function
"""


def test_no_path(instance):
    assert instance.default("¯\\_(ツ)_/¯") == sample_data


def test_default_is_returned_if_path_doesnt_exist(instance):
    default_val = "hello world"
    assert instance.default(default_val, 1, 2, 3, 4) == default_val


def test_actual_value_is_returned(instance):
    assert instance.default("uuuuh idek", "widget", "window", "height") == sample_data["widget"]["window"]["height"]
