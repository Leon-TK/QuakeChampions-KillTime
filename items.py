from abc import ABC, abstractmethod

class IItem(ABC):
    pass

class ItemBase():
    pass

class Armor(ItemBase, IItem):
    def __init__(self) -> None:
        ItemBase.__init__(self)
        self.value = 0

class Health(ItemBase, IItem):
    def __init__(self) -> None:
        ItemBase.__init__(self)
        self.value = 0

class Mega(Health, IItem):
    def __init__(self) -> None:
        ItemBase.__init__(self)
        self.value = 100
        self.overValue = 75

class Red(Armor, IItem):
    def __init__(self) -> None:
        ItemBase.__init__(self)
        self.value = 100
        self.overValue = 75

class Blob(Health, IItem):
    def __init__(self) -> None:
        ItemBase.__init__(self)
        self.value = 100

class Yellow(Armor, IItem):
    def __init__(self) -> None:
        ItemBase.__init__(self)
        self.value = 100
# 5 armor
class Shard(Armor, IItem):
    def __init__(self) -> None:
        ItemBase.__init__(self)
        self.value = 100