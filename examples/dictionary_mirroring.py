from constload import ConstantLoader

k = ConstantLoader("../tests/resources/sample.json")

print(k.data["widget"]["text"].get("this-does-not-exist"))

SAMPLE = k.default(("widget", "text", "this-does-not-exist"), "Sure about that?")

print(k.data["widget"]["text"].get("this-does-not-exist"))
