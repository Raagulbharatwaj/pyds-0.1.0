from pyds.node import ListNode, DoubleListNode


class LinkedList:

    def __init__(self, x):
        self._head = ListNode(data=x)
        self._len  = 1

    def __getitem__(self, item):
        if item == "head":
            return self._head

    def __str__(self):
        temp = self._head
        x = str(temp["data"])+" "
        while temp["next"] is not None:
            temp = temp["next"]
            x += str(temp["data"])+" "
        return x

    def append(self, x):
        curr = self._head
        while curr["next"] is not None:
            curr = curr["next"]
        curr["next"] = ListNode(data=x)
        self._len += 1

    def extend(self, x):
        curr = self._head
        while curr["next"] is not None:
            curr = curr["next"]
        for i in x:
            curr["next"] = ListNode(data=i)
            curr = curr["next"]
            self._len += 1

    def insert(self, x, pos):
        if pos > self._len:
            raise RuntimeError(f"Unable to insert {x} at {pos} as length of the list object at 0x{id(self)} is {self._len}")
        if pos == 0:
            new = ListNode(data=x, next_=self._head)
            self._head = new
            self._len += 1
        elif pos == self._len:
            self.append(x)
        else:
            curr = self._head
            count = 0
            while count < pos-1 and curr["next"] is not None:
                curr = curr["next"]
                count += 1
            new = ListNode(data=x, next_=curr["next"])
            curr["next"] = new
            self._len += 1

    def delete(self, x):
        curr = self._head
        if curr["data"] == x:
            self._head = curr["next"]
            curr["next"] = None
            return
        while curr["next"]["data"] != x and curr["next"] is not None:
            curr = curr["next"]
        if curr["next"] is None:
            return -1
        else:
            temp = curr["next"]
            curr["next"] = temp["next"]
            temp["next"] = None
            return 1

    def mid(self):
        slow = self._head
        fast = self._head
        while fast is not None and fast["next"] is not None:
            slow = slow["next"]
            fast = fast["next"]["next"]
        return slow["data"]


class DoublyLinkedList:
    def __init__(self, x):
        self._head = DoubleListNode(data=x)
