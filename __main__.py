from actions import handle_user_input
from color import green
from game import Game
from player import Player
from location import game_locations
from with_items import ObjectWithItems

new_player = Player(ObjectWithItems('Ricky'), game_locations['start'])
game = Game(new_player)
game.game_start()

# GAMEPLAY LOOP
while True:
    game.player.loc.seen = True
    game.player.loc.show_items()
    game.player.show_items()

    # await user input
    action = input(f'{green('$ Action: ')}').strip()
    if action:
        handle_user_input(game, action)
