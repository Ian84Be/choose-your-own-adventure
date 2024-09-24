import re
from color import green, purple, red
from item import get_item_desc, item_toy


ACT_LOOK = 'LOOK'
ACT_GO = 'GO'
ACT_GET = 'GET'
ACT_USE = 'USE'
ACT_DROP = 'DROP'
game_actions = [ACT_LOOK, ACT_GO, ACT_GET, ACT_USE, ACT_DROP]
item_actions = [ACT_LOOK, ACT_GET, ACT_USE, ACT_DROP]
valid_directions = {'NORTH', 'EAST', 'WEST', 'SOUTH', 'UP', 'DOWN'}


def action_help():
    print(f'{red(ACT_LOOK)} '
          f'{green('$ Observe your surroundings')}')

    print(f'{red(ACT_GO)} '
          f'[{purple(valid_directions)}] '
          f'{green('$ Move in that direction (ex. go ')}'
          f'{purple('NORTH')}'
          )

    print(f'{red(ACT_GET)} '
          f'[{red('item')}] '
          f'{green('$ Pick up an item you see (ex. get Rubber Duck)')}')

    print(f'{red(ACT_USE)} '
          f'[{red('item')}] '
          f'{green('$ Use an item you are holding(ex. use Flashlight)')}')

    print(f'{red(ACT_DROP)} '
          f'[{red('item')}] '
          f'{green('$ Drop an item you are holding (ex. drop Flashlight)')}')

    print(f'{red('Q')} '
          f'{green('$ Quit')}')


def do_nothing_message(act):
    return f'Nothing... You {green(act)} NOTHING...'


def handle_user_input(game, action):
    user_input = re.match(r'([a-z]*)\s*([a-z]*)', action, flags=re.I)
    input_1 = user_input.group(1).upper()
    input_2 = user_input.group(2)

    if input_1 in {'Q', 'QUIT'}:
        return game.game_over()
    if input_1 in {'H', 'HELP'}:
        return action_help()
    if input_1 not in game_actions:
        return print(f'\n\n{green(input_1)} {red('cannot be done.')}\n\n'
                     f'type {purple('HELP')} to see a list of actions\n\n')
    return handle_action(game, input_1, input_2)


def find_item(player, subject):
    player_has_item = player.find_item(subject)
    loc_has_item = player.loc.find_item(subject)
    item_found = player_has_item or loc_has_item
    return item_found, player_has_item, loc_has_item


def handle_action(game, verb, subject):
    player = game.player
    has_subject = subject != ''
    if has_subject:
        subject = subject.upper()

    item_desc = get_item_desc(subject)
    item_found, player_has_item, loc_has_item = find_item(player, subject)
    item_not_found = has_subject and verb in item_actions and not item_found
    item_not_found_message = f'{red(subject)} not found.'
    if item_not_found:
        print(item_not_found_message)

    direction_not_found = verb == ACT_GO and has_subject and subject not in valid_directions
    direction_not_found_message = (f'GO {red(subject)}? Not possible.'
                                   'Please GO in a valid direction.')
    if direction_not_found:
        print(direction_not_found_message)
        print(valid_directions)

    if verb != ACT_LOOK and not has_subject:
        print(do_nothing_message(verb))

    if verb == ACT_LOOK:
        if not has_subject:
            print(player.loc)
        elif subject == 'SELF':
            print(str(player))
        elif item_found:
            print(item_desc)

    if verb == ACT_GET:
        if loc_has_item:
            player.loc.act_get(player, subject)
            if subject == item_toy.name:
                game.rubber_duck_death()

    if verb == ACT_DROP:
        if player_has_item:
            player.act_drop(subject)

    if verb == ACT_USE:
        if player_has_item:
            player.loc.act_use(subject)

    if verb == ACT_GO:
        player.loc.act_go(player, subject)
