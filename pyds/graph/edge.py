class edge:
    __properties = {}

    def __init__(self, propdict):
        edge.__properties = propdict

    def __getitem__(self, key):
        return edge.__properties[key]

    def __setitem__(self, key, value):
        edge.__properties[key] = value

