from abc import ABC, abstractmethod


class Box(ABC):
    @abstractmethod
    def add(self):
        ...

    @abstractmethod
    def empty(self):
        ...

    @abstractmethod
    def count(self):
        ...


class Item:
    def __init__(self, name, value):
        self.name = name
        self.value = value


class DictBox(Box):
    def __init__(self):
        self.dict_elem = {}

    def add(self, *other):
        self.dict_elem.update({(x, x.value): x for x in other})

    def empty(self):
        elem = list(self.dict_elem.values())
        self.dict_elem = {}
        return elem

    def count(self):
        return len(self.dict_elem)


class ListBox(Box):
    def __init__(self):
        self.list_elem = []

    def add(self, *other):
        self.list_elem += other

    def empty(self):
        elem = self.list_elem
        self.list_elem = []
        return elem

    def count(self):
        return len(self.list_elem)


def repack_boxes(*box):
    box_elem = []
    for i in box:
        box_elem.extend(i.empty())
    k = len(box_elem)
    while k > 0:
        for i in box:
            try:
                i.add(box_elem[0])
                box_elem = box_elem[1:]
                k -= 1
            except IndexError:
                break


box1 = ListBox()
box1.add(*[Item(str(i), i) for i in range(20)])
box2 = ListBox()
box2.add(*[Item(str(i), i) for i in range(9)])
box3 = DictBox()
box3.add(*[Item(str(i), i) for i in range(5)])
print(box1.count(), box2.count(), box3.count())
repack_boxes(box1, box2, box3)
print(box1.count(), box2.count(), box3.count())
