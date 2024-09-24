from color import red
from with_items import ObjectWithItems, WithItems


class Player(WithItems):
    def __init__(self, obj: ObjectWithItems, loc):
        super().__init__(obj)
        self.loc = loc

    def __str__(self):
        return f'++ {self.name} is at the {self.loc.name} ++'

    def show_items(self):
        print(f'You are holding {red(self.show_items_text())}\n')

    def act_get(self, item):
        print(f'You pick up the {red(item.name)}')
        if self.holding:
            self.holding.append(item)
        else:
            self.holding = [item]

    def act_drop(self, subject):
        print(f'You dropped the {red(subject)}')
        item_names = self.get_item_names()
        if item_names:
            index = item_names.index(subject)
            item = self.holding.pop(index)
            self.loc.act_drop(item)
