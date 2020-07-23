import json as _json
import yaml
try:
    from yaml import CLoader as yaml_loader
except ImportError:
    from yaml import Loader as yaml_loader


class Loaders:
    @classmethod
    def json(_, data):
        return _json.loads(data)

    @classmethod
    def yaml_safe(_, data):
        return yaml.safe_load(data)

    @classmethod
    def yaml_unsafe(_, data):
        return yaml.load(data, Loader=yaml_loader)
