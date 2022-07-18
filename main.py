from pyds.vector.vect import NDVector

x = NDVector(dim=3, init=1)
y = NDVector(dim=3, init=2)
print(NDVector.euclidian_distance(x, y))

