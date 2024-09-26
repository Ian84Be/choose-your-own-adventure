from dataclasses import dataclass
from game.actions import ACT_GO, ACT_LOOK, ACT_USE
from .color import green, red, purple
from .game import crawl_text
from .with_items import ObjectWithItems, WithItems
from .item import item_key, item_toy, item_flashlight, item_napkin


class Location(WithItems):
    def __init__(self, obj: ObjectWithItems, use_items=None, is_dark=False):
        super().__init__(obj)
        self.use_items = use_items
        self.is_dark = is_dark
        self.seen = False
        self.connections = LocationConnections(
            n_to=None,
            e_to=None,
            s_to=None,
            w_to=None,
            u_to=None,
            d_to=None
        )

    def __str__(self):
        return f'{self.desc}\n'

    def show_items(self):
        if self.is_dark:
            crawl_text(f'In {red('darkness...')}')
        elif self.show_items_text():
            crawl_text(f'You can see {red(self.show_items_text())}')

    def act_look(self):
        crawl_text(f'{purple(self.name)}', 0.05)
        crawl_text(self.desc+'\n', 0.03)

    def act_get(self, player, subject):
        if self.is_dark:
            crawl_text(f'It is too {red('dark')} to see anything.')
        else:
            loc_item_names = self.get_item_names()
            index = loc_item_names.index(subject)
            item = self.holding.pop(index)
            player.act_get(item)

    def act_drop(self, item):
        if self.holding:
            self.holding.append(item)
        else:
            self.holding = [item]

    def get_use_item_names(self):
        if self.use_items:
            return self.use_items.keys()
        return None

    def act_use(self, subject):
        use_item_names = self.get_use_item_names()
        crawl_text(f'You {green(ACT_USE)} '
                   f'the {red(subject)}', 0.05)
        if use_item_names:
            if subject == item_flashlight.name:
                self.is_dark = False
            crawl_text(self.use_items[subject]+'\n', 0.03)
        else:
            crawl_text('Nothing happened...\n', 0.03)

    def act_go(self, player, direction):
        go_to = direction[0].lower() + '_to'
        new_loc = getattr(self.connections, go_to)
        if new_loc is None:
            crawl_text('No...')
            crawl_text(f'You cannot {green(ACT_GO+' '+direction)} from here.')
        if new_loc is not None:
            player.loc = new_loc
            crawl_text(f'You {green(ACT_GO+' '+direction)} '
                       f'to {purple(new_loc.name)}\n', 0.05)
            if player.loc.seen is False:
                player.loc.seen = True
                crawl_text(player.loc.desc, 0.03)
            else:
                crawl_text(purple('You have been here before...\n'), 0.03)
                print(player.loc.desc)
                print('\n')
                crawl_text(f'{purple(player.loc.name)}', 0.03)


@dataclass
class LocationConnections:
    n_to: Location = None
    e_to: Location = None
    s_to: Location = None
    w_to: Location = None
    u_to: Location = None
    d_to: Location = None


# DRAMATIC INTRO
game_start_text = ('Your body is aching and your pants are wet with mud. '
                   'You are curled up in a fetal position, touching grass.\r'
                   f'You stand up and {purple(ACT_LOOK)} around.\r'
                   'You see an iron gate behind you, '
                   'and a gravel pathway before you.\r'
                   'How did you get here? '
                   'You touch your head and feel a lump. '
                   'It is wet, and sticky.\r'
                   f'You see a {red(item_flashlight.name)} on the ground. '
                   f'It\'s {purple('*YOUR*')} {red(item_flashlight.name)}.')
game_start_room = Location(ObjectWithItems('You awaken suddenly', game_start_text,
                           [item_flashlight]))

# create LOCATIONS
outside_text = (f'To the {purple('NORTH')} you see a gravel pathway lined with trees.\n'
                f'The iron gate to the {purple('SOUTH')} is locked, '
                'and topped with several layers of razor wire.\n'
                'Somebody is serious about home security.')
outside_room = Location(
    ObjectWithItems('Outer gate', outside_text))

gravel_text = (f'Lawns stretch out to either side, '
               'but you cannot see much beyond the large oak trees lining the pathway. '
               f'To the {purple('NORTH')} '
               'you see the shape of a building. '
               'You walk further down the noisy gravel path until the shape comes into focus, '
               'You see a decrepit looking white mansion in the colonial style. '
               'You can hear something moving around nearby.')
gravel_use_items = {
    'FLASHLIGHT': ('You see a large dog moving beyond the trees.\n'
                   'You shine the FLASHLIGHT directly into his eyes.\n'
                   'He stops for a moment, stunned.\n'
                   'You follow him with the FLASHLIGHT as he lets out a short bark and runs away.\n'
                   'That is the biggest dog you\'ve ever seen.\n')

}
gravel_room = Location(ObjectWithItems(
    'Gravel pathway', gravel_text), use_items=gravel_use_items, is_dark=True)

lawn_text = (f'{purple('NORTH')} of you, '
             'the door to the mansion is wide open.  '
             f'What happened here? It is {red('DARK')}, '
             'but you can see several large holes dug into the lawn. '
             'You still hear something moving around, out of sight.')
lawn_use_items = {
    'FLASHLIGHT': ('You shine the light around the muddy holes in the lawn. '
                   'A flash of yellow catches your eye. It looks like some kind of dog toy.')
}
lawn_room = Location(ObjectWithItems('Front lawn of the mansion', lawn_text,
                                     [item_toy]), use_items=lawn_use_items, is_dark=True)

foyer_text = ('This room is mostly empty space surrounding a grand staircase, '
              f'a few steps are missing but you could climb {purple('UP')}. '
              f'Dusty passages run {purple('EAST')} and {purple('WEST')}. ')

ballroom_text = ('You admire the polished hardwood floors. '
                 'One of the chandeliers has fallen.'
                 'Crystal shrapnel radiates from the far end of the room. '
                 f'The only exit is {purple('DOWN')} the staircase.')
ballroom_room = Location(ObjectWithItems('Grand ballroom', ballroom_text,
                                         [item_napkin]))

library_text = ('You stand among thousands of years of collected thoughts. '
                'Bookshelves line every wall but they are all emptied. '
                'Someone has recently searched this room. '
                'Books and furniture lay tossed about in various piles. '
                f'The only exit is {purple('EAST')}.')

narrow_text = (f'The narrow passage bends here from {purple('WEST')} to {purple('NORTH')}.  '
               'The smell of lavender permeates the air.')


treasure_text = (f'You see a large door, engraved with mysterious symbols. '
                 'It seems to be made from solid gold, and feels warm to the touch. '
                 f'There is a large [{red('KEYHOLE')}] in the center. '
                 f'The only exit is to the {purple('SOUTH')}.')
treasure_use_items = {
    'KEY': ('You hesitate for a moment, '
            'contemplating the strange engravings on this golden door. '
            'You feel the warmth of the key in your hand as it turns with a satisfying '
            f'{purple('*CLICK*')}')
}
treasure_room = Location(ObjectWithItems('Treasure chamber', treasure_text,
                                         [item_key]), use_items=treasure_use_items)

game_locations = {
    'start': game_start_room,
    'outside': outside_room,
    'gravel': gravel_room,
    'lawn': lawn_room,
    'foyer': Location(ObjectWithItems('Foyer', foyer_text)),
    'ballroom': ballroom_room,
    'library': Location(ObjectWithItems('Library', library_text)),
    'narrow': Location(ObjectWithItems('Narrow passage', narrow_text)),
    'treasure': treasure_room,
}

# connect LOCATIONS
game_locations['start'].connections = LocationConnections(
    n_to=game_locations['outside']
)

game_locations['outside'].connections = LocationConnections(
    n_to=game_locations['gravel'],
)

game_locations['gravel'].connections = LocationConnections(
    n_to=game_locations['lawn'],
    s_to=game_locations['outside'],
)

game_locations['lawn'].connections = LocationConnections(
    n_to=game_locations['foyer'],
    s_to=game_locations['gravel'],
)

game_locations['foyer'].connections = LocationConnections(
    n_to=game_locations['foyer'],
    s_to=game_locations['lawn'],
    u_to=game_locations['ballroom'],
)

game_locations['ballroom'].connections = LocationConnections(
    d_to=game_locations['foyer'],
)

game_locations['foyer'].connections = LocationConnections(
    e_to=game_locations['narrow'],
    w_to=game_locations['library'],
)

game_locations['library'].connections = LocationConnections(
    e_to=game_locations['foyer'],
)

game_locations['narrow'].connections = LocationConnections(
    n_to=game_locations['treasure'],
    w_to=game_locations['foyer'],
)

game_locations['treasure'].connections = LocationConnections(
    s_to=game_locations['narrow'],
)
