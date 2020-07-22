import json
import os

import pytest
import constload

"""
Checks to test initialisation
"""

sample_json_filepath = "tests/resources/sample.json"
sample_yaml_filepath = "tests/resources/sample.yml"

raw_sample_data = open(sample_json_filepath).read()
sample_data = json.loads(raw_sample_data)


def test_from_file():
    k = constload.ConstantLoader(sample_json_filepath)
    assert k.data == sample_data


def test_from_string():
    k = constload.ConstantLoader(raw_sample_data)
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
