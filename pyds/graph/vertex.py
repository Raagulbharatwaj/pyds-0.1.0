class vertex:
    __properties = {}
    __neighbours = {}

    def __init__(self, propdict, neighbourdict={}):
        if neighbourdict is None:
            neighbourdict = {}
        vertex.__properties = propdict
        vertex.__neighbours = neighbourdict

    def __getitem__(self, key):
        if key == "neighbours":
            return [neighbour for neighbour in vertex.__neighbours]
        return vertex.__properties[key]

    def __setitem__(self, key, value):
        if key == "neighbours" and type(value) != dict:
            raise SyntaxError(
                f"Incompatible datatype expected a type {type(vertex.__neighbours)} whereas got a{type(value)}")
        elif key == "neighbour" and type(value) == dict:
            vertex.__neighbours = value
        else:
            vertex.__properties[key] = value