from constload import ConstantLoader

k = ConstantLoader("../tests/resources/sample.json")

WINDOW_HEIGHT = k.required(("widget", "window", "height"))
WINDOW_WIDTH = k.required(("widget", "window", "width"))
TEXT_DATA = k.default(("widget", "text", "hello-does-this-exist?"))  # Default default value is None

print(WINDOW_WIDTH, WINDOW_HEIGHT, TEXT_DATA)