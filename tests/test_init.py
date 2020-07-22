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


def test_yaml():
    k = constload.ConstantLoader(sample_yaml_filepath)
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
