from .actions import handle_user_input
from .color import green
from .game import Game
from .player import Player
from .location import game_locations
from .with_items import ObjectWithItems
from .item import item_toy

new_player = Player(ObjectWithItems('Ricky'), game_locations['start'])
game = Game(new_player)
game.game_start()

# GAMEPLAY LOOP
while True:
    if item_toy in game.player.holding:
        game.rubber_duck_death()

    game.player.loc.show_items()
    game.player.show_items()

    # await user input
    action = input(f'{green('$ Action: ')}')
    action.strip()
    if action:
        handle_user_input(game, action)
