from game.game import crawl_text
from .color import green, purple, red
from .with_items import ObjectWithItems, WithItems


class Player(WithItems):
    def __init__(self, obj: ObjectWithItems, loc):
        super().__init__(obj)
        self.loc = loc

    def __str__(self):
        return f'++ {self.name} is at the {self.loc.name} ++'

    def show_items(self):
        if self.holding:
            crawl_text(f'You are holding {red(self.show_items_text())}\n')

    def act_get(self, item):
        crawl_text(f'You {green('GET')} the {red(item.name)}\n', 0.05)
        crawl_text(f'{purple(item.desc)}', 0.03)
        if self.holding:
            self.holding.append(item)
        else:
            self.holding = [item]

    def act_drop(self, subject):
        crawl_text(f'You {green('DROP')} the {red(subject)}', 0.05)
        item_names = self.get_item_names()
        if item_names:
            index = item_names.index(subject)
            item = self.holding.pop(index)
            self.loc.act_drop(item)
