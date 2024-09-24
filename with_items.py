from dataclasses import dataclass
from object import Object


@dataclass
class ObjectWithItems:
    name: str
    desc: str = 'N/A'
    holding: list = None


class WithItems(Object):
    def __init__(self, obj: ObjectWithItems):
        super().__init__(obj.name, obj.desc)
        self.holding = obj.holding

    def get_item_names(self):
        item_names = None
        if self.holding is not None:
            item_names = [item.name for item in self.holding]
        return item_names

    def show_items_text(self):
        my_items = self.get_item_names()
        if not my_items:
            my_items = 'nothing'
        return my_items

    def find_item(self, subject):
        item_names = self.get_item_names()
        found = item_names and subject in item_names
        return found
