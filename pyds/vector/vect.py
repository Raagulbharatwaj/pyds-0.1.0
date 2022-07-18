import math


class NDVector:

    def __init__(self, dim=-1, init=0, init_list=None):
        if init_list is None and dim == -1:
            self._ele = [init]*2
            self._dim = 2
        elif init_list is not None and dim == -1:
            self._ele = init_list
            self._dim = len(init_list)
        elif init_list is not None and dim>=0:
            self._dim = dim
            self._ele = init_list[:dim]
        else:
            self._ele = [init]*dim
            self._dim = len(self._ele)

    def __getitem__(self, item):
        if item == "dim":
            return self._dim
        elif item == "ele":
            return self._ele
        else:
            raise RuntimeError(f"{type(self)} does not have an attribute called as {item}")

    def __str__(self):
        x = ""
        for i in self._ele:
            x += f"{i} "
        return x

    def __add__(self, other):
        if type(other) != type(self):
            y = []
            for i in range(self._dim):
                y.append(self._ele[i]+other)
            return NDVector(init_list=y)
        else:
            if self._dim != other["dim"]:
                raise TypeError(f"{type(self)} object at 0x{id(self)} and {type(other)} object at 0x{id(other)} has incompatible dimensions to add")

            x = [0]*self._dim
            y = other["ele"]
            for i in range(self._dim):
                x[i] = self._ele[i] + y[i]
            z = NDVector(init_list=x)
            return z

    def __iadd__(self, other):
        if type(other) != type(self):
            for i in range(self._dim):
                self._ele[i] += other
            return self
        else:
            if self._dim != other["dim"]:
                raise TypeError(f"{type(self)} object at 0x{id(self)} and {type(other)} object at 0x{id(other)} has incompatible dimensions to add")
            y = other["ele"]
            for i in range(self._dim):
                self._ele[i] += y[i]
            return self

    def __mul__(self, other):
        if type(other) != type(self):
            y = []
            for i in range(self._dim):
                y.append(self._ele[i]*other)
            return NDVector(init_list=y)
        else:
            if self._dim != other["dim"]:
                raise TypeError(
                    f"{type(self)} object at 0x{id(self)} and {type(other)} object at 0x{id(other)} has incompatible dimensions to add")
            x = 0
            y = other["ele"]
            for i in range(self._dim):
                x += self._ele[i] * y[i]
            return x

    def __imul__(self, other):
        if type(other) != type(self):
            for i in range(self._dim):
                self._ele[i] *= other
            return self
        else:
            raise TypeError(f"Invalid operation between operands of {type(self)}")

    def norm(self):
        y = 0
        for i in self._ele:
            y += i**2
        return math.sqrt(y)

    def proj(self, x):
        dot = self*x
        norm = x.norm()
        return dot/norm

    def project(self, x):
        p = (self*x)/(x.norm()**2)
        y = x["ele"]
        z = []
        for i in y:
            z.append(i*p)
        projected = NDVector(init_list=z)
        return projected

    @staticmethod
    def euclidian_distance(x, y):
        if type(x) != type(y) != NDVector:
            raise TypeError(f"Cannot find Euclidian distance between elements of {type(x)} and {type(y)}")
        else:
            if x["dim"] != y["dim"]:
                raise TypeError(
                    f"{type(x)} object at 0x{id(x)} and {type(y)} object at 0x{id(y)} has incompatible dimensions to add")
            a = x["ele"]
            b = y["ele"]
            dist = 0
            for i in range(len(a)):
                dist += (a[i]-b[i])**2
        return math.sqrt(dist)

    @staticmethod
    def manhattan_distance(x,y):
        if type(x) != type(y) != NDVector:
            raise TypeError(f"Cannot find Euclidian distance between elements of {type(x)} and {type(y)}")
        else:
            if x["dim"] != y["dim"]:
                raise TypeError(
                    f"{type(x)} object at 0x{id(x)} and {type(y)} object at 0x{id(y)} has incompatible dimensions to add")
            a = x["ele"]
            b = y["ele"]
            dist = 0
            for i in range(len(a)):
                dist += abs(a[i] - b[i])
        return math.sqrt(dist)



