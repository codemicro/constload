from .constants import *
import pytest
import constload

"""
To test the ConstLoader.pick_default function
"""


def test_no_path(instance):
    assert instance.pick_default("¯\\_(ツ)_/¯") == sample_data


def test_default_is_returned_if_path_doesnt_exist(instance):
    default = "hello world"
    assert instance.pick_default(default, 1, 2, 3, 4) == default


def test_actual_value_is_returned(instance):
    assert instance.pick_default("uuuuh idek", "widget", "window", "height") == sample_data["widget"]["window"]["height"]
