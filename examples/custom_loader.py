from constload import ConstantLoader


data = "id,name,country\n0,John Doe,Ireland\n1,Miles Walsh,USA\n2,Andrew Peebles,Scotland"


def loader(data):
    # Basic CSV loader
    my_dict = {}
    lines = data.split("\n")[1:]
    for line in lines:
        vals = line.split(",")
        my_dict[vals[0]] = {"name": vals[1], "country": vals[2]}
    return my_dict


c = ConstantLoader(data, loader=loader)

print(c.data)
