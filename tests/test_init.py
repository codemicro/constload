import random

from .constants import *
import pytest
import constload

"""
Checks to test initialisation
"""

def test_from_file():
    k = constload.ConstantLoader(sample_json_filepath)
    assert k.data == sample_data


def test_from_string():
    k = constload.ConstantLoader(raw_json_data)
    assert k.data == sample_data


def test_yaml_safe():
    k = constload.ConstantLoader(sample_yaml_filepath)
    assert k.data == sample_data


def test_yaml_unsafe():
    k = constload.ConstantLoader(sample_yaml_filepath, safe_load_yaml=False)
    assert k.data == sample_data


def test_preloaded_data():
    k = constload.ConstantLoader(sample_data)
    assert k.data == sample_data


def test_invalid_datatype():
    with pytest.raises(TypeError):
        constload.ConstantLoader(1234)

    with pytest.raises(TypeError):
        constload.ConstantLoader(["hi there"])

    with pytest.raises(TypeError):
        constload.ConstantLoader(tuple("this is a tuple".split(" ")))


def test_custom_loader():
    data = {"hello": "world", "random": random.randint(0, 2000)}
    k = constload.ConstantLoader(raw_json_data, loader=(lambda x: data))
    assert k.data == data


def test_custom_loader_no_return_value():
    with pytest.raises(ValueError):
        constload.ConstantLoader(raw_json_data, loader=(lambda x: None))


def test_custom_loader_bad_return_value():
    with pytest.raises(ValueError):
        constload.ConstantLoader(raw_json_data, loader=(lambda x: "this really isn't a dictionary"))
