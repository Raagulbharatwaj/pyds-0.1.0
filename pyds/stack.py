class Stack:

    def __init__(self, arr=[]):
        self._data = arr

    def __len__(self):
        return len(self._data)

    def push(self, x):
        self._data.append(x)

    def empty(self):
        return len(self._data) == 0

    def pop(self):
        if self.empty():
            raise RuntimeError("Trying to pop a stack object at OX{} which is already empty".format(id(self)))
        else:
            x = self._data[-1]
            self._data.pop(-1)
            return x

    def top(self):
        if self.empty():
            raise RuntimeError("Stack object at OX{} is empty".format(id(self)))
        else:
            return self._data[-1]

    def __str__(self):
        x = ""
        for i in range(len(self._data) - 1, -1, -1):
            x += str(self._data[i]) + " "
        return x

    def flush(self):
        self._data = []

