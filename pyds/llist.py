from pyds.node import ListNode, DoubleListNode


class LinkedList:

    __root = None

    def __init__(self, x):
        LinkedList.__root = ListNode(data=x)

    def append(self, x):
        curr = LinkedList.__root
        while curr["next"] is not None:
            curr = curr["next"]
        curr["next"] = ListNode(data=x)

    def extend(self, x):
        curr = LinkedList.__root
        while curr["next"] is not None:
            curr = curr["next"]
        for i in x:
            curr["next"] = ListNode(data=i)
            curr = curr["next"]