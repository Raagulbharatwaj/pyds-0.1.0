from pyds.node import TreeNode
from pyds.quene import Queue


class BinaryTree:

    def __init__(self, x):
        if x is None:
            raise TypeError(f"Cannot assign an object of type {type(x)} to {TreeNode}")
        self._root = TreeNode(data=x)

    def __getitem__(self, item):
        if item == "root":
            return self._root

    def __str__(self):
        curr = self._root
        x = str(curr["data"])+" "
        q = Queue()
        if curr["left"] is not None:
            q.enqueue(curr["left"])
        if curr["right"] is not None:
            q.enqueue(curr["right"])
        while not q.empty():
            temp = q.dequeue()
            if temp is not None:
                x += str(temp["data"])+" "
                if temp["left"] is not None:
                    q.enqueue(temp["left"])
                if curr["right"] is not None:
                    q.enqueue(temp["right"])
        return x

    def insert(self, x):
        if self._root["data"] is None:
            self._root["data"] = x
        else:
            curr = self._root
            while True:
                if x >= curr["data"] and curr["right"] is None:
                    curr["right"] = TreeNode(data=x)
                    break
                elif x >= curr["data"] and curr["right"] is not None:
                    curr = curr["right"]
                    continue
                elif x < curr["data"] and curr["left"] is None:
                    curr["left"] = TreeNode(data=x)
                    break
                elif x < curr["data"] and curr["left"] is not None:
                    curr = curr["left"]
                    continue
                else:
                    raise RuntimeError(f"Process Terminated Due to untraceable error check if the nodes have same data type")




