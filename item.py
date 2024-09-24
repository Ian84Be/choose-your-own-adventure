from color import red
from object import Object


class Item(Object):
    def __init__(self, name, desc, seen=False):
        super().__init__(name, desc)
        self.seen = seen


flashlight_desc = ('Your trusty MagLite. '
                   'Alloy steel packed with D-cell batteries. '
                   '1000 lumens of blinding power.')
item_flashlight = Item('FLASHLIGHT', flashlight_desc)

napkin_desc = ('It is a map, hastily drawn on a used napkin. '
               'You don\'t recognize the symbols, '
               'but there are a few letters written in pencil: '
               f'{red('W N W N E')}')
item_napkin = Item('NAPKIN', napkin_desc)

item_key = Item(
    'KEY', 'An unusally large, metal key. Feels warm to the touch.')
item_toy = Item(
    'TOY', 'A well loved toy. Bright yellow, dripping with dog slobber.')

game_items = [item_key, item_toy, item_flashlight, item_napkin]
item_names = [item.name for item in game_items]


def get_item_desc(subject):
    unknown_subject = subject not in item_names
    item_desc = ''
    if not unknown_subject:
        item_index = item_names.index(subject)
        item_desc = str(game_items[item_index])
    return item_desc
