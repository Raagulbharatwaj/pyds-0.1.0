class Queue:

    def __init__(self, arr=None, size=None):
        if arr is None:
            arr = []
        self._data = arr
        self._size = size

    def __len__(self):
        return len(self._data)

    def empty(self):
        return len(self) == 0

    def front(self):
        if self.empty():
            raise RuntimeWarning(f"Cannot display the front as Queue object at Ox{id(self)} is empty")
        return self._data[0]

    def rear(self):
        if self.empty():
            raise RuntimeWarning(f"Cannot display the rear as Queue object at Ox{id(self)} is empty")
        return self._data[-1]

    def enqueue(self, x):
        if self._size is not None and len(self) == self._size:
            raise RuntimeError(f"Cannot enqueue the elements to queue at Ox{id(self)} as the queue is at its full capacity")
        else:
            self._data.append(x)

    def dequeue(self):
        if self.empty():
            raise RuntimeWarning(f"Cannot perform dequeue operation as Queue object at Ox{id(self)} is empty")
        x = self._data[0]
        self._data.pop(0)
        return x

    def __str__(self):
        x = ""
        for i in self._data:
            x += str(i) + " "
        return x

    def flush(self):
        self._data = []

