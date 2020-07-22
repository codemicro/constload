from .constants import *
import pytest
import constload

"""
To test the ConstLoader.get_required_option function
"""


def test_no_path(instance):
    assert instance.get_required_option() == sample_data


def test_default_is_returned_if_path_doesnt_exist(instance):
    with pytest.raises(constload.exceptions.RequiredSettingNotFoundException):
        instance.get_required_option(1, 2, 3, 4)


def test_actual_value_is_returned(instance):
    assert instance.get_required_option("widget", "window", "height") == sample_data["widget"]["window"]["height"]