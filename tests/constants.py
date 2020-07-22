import json
import pytest
import constload


@pytest.fixture(scope="module")
def instance():
    k = constload.ConstantLoader(sample_data)
    yield k


sample_json_filepath = "tests/resources/sample.json"
sample_yaml_filepath = "tests/resources/sample.yml"

raw_json_data = open(sample_json_filepath).read()
sample_data = json.loads(raw_json_data)
