
class ListNode:

    def __init__(self, data=None, next_=None):
        self._data = data
        self._next = next_

    def __getitem__(self, item):
        if item == "next":
            return self._next
        elif item == "data":
            return self._data
        else:
            raise RuntimeError(f"ListNode Does not have any attribute called {item}")

    def __setitem__(self, key, value):
        if key == "next" and (type(value) == type(self) or value is None):
            self._next = value
        elif key == "next" and type(value) != type(self) and value is not None:
            raise TypeError(f"Expected an argument of type {type(self)} whereas got an argument of type {type(value)}")
        elif key == "data":
            self._data = value
        else:
            raise RuntimeError(f"ListNode Does not have any attribute called {key}")

    @staticmethod
    def swap(instance1, instance2):
        instance1["data"], instance2["data"] = instance2["data"], instance1["data"]

    def reset_node(self):
        self._data = None
        self._next = None


class DoubleListNode:

    def __init__(self, data=None, next_=None, prev=None):
        self._data = data
        self._next = next_
        self._prev = prev

    def __getitem__(self, item):
        if item == "next":
            return self._next
        elif item == "data":
            return self._data
        elif item == "prev":
            return self._prev
        else:
            raise RuntimeError(f"DoubleListNode Does not have any attribute called {item}")

    def __setitem__(self, key, value):
        if key == "next" and (type(value) == type(self) or value is None):
            self._next = value
        elif key == "next" and type(value) != type(self) and value is not None:
            raise TypeError(f"Expected an argument of type {type(self)} whereas got an argument of type {type(value)}")
        elif key == "prev" and (type(value) == type(self) or value is None):
            self._prev = value
        elif key == "prev" and type(value) != type(self) and value is not None:
            raise TypeError(f"Expected an argument of type {type(self)} whereas got an argument of type {type(value)}")
        elif key == "data":
            self._data = value
        else:
            raise RuntimeError(f"DoubleListNode Does not have any attribute called {key}")

    @staticmethod
    def swap(instance1, instance2):
        instance1["data"], instance2["data"] = instance2["data"], instance1["data"]

    def reset_node(self):
        self._data = None
        self._next = None
        self._prev = None


class TreeNode:

    def __init__(self, data=None, left=None, right=None):
        self._data  = data
        self._left  = left
        self._right = right

    def __getitem__(self, item):
        if item == "data":
            return self._data
        elif item == "left":
            return self._left
        elif item == "right":
            return self._right
        else:
            raise RuntimeError(f"TreeNode Does not have any attribute called {item}")

    def __setitem__(self, key, value):
        if key == "left" and (type(value) == type(self) or value is None):
            self._left = value
        elif key == "left" and type(value) != type(self) and value is not None:
            raise TypeError(f"Expected an argument of type {type(self)} whereas got an argument of type {type(value)}")
        elif key == "right" and (type(value) == type(self) or value is None):
            self._right = value
        elif key == "right" and type(value) != type(self) and value is not None:
            raise TypeError(f"Expected an argument of type {type(self)} whereas got an argument of type {type(value)}")
        elif key == "data":
            self._data = value
        else:
            raise RuntimeError(f"ListNode Does not have any attribute called {key}")

    def reset_node(self):
        self._data  = None
        self._left  = None
        self._right = None
