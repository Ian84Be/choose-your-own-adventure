import sys
import time
from textwrap import wrap
from .actions import ACT_GET, ACT_GO, ACT_LOOK, handle_action
from .color import green, purple, red
from .item import item_flashlight


def crawl_text(text, delay=0.01):
    text = wrap(text, 80)
    text = '\n'.join(text)
    for ln in text:
        print(ln, end='', flush=True)
        time.sleep(delay)
    print('\n')


class Game:
    def __init__(self, player):
        self.player = player

    def game_start(self):
        handle_action(self, ACT_LOOK, '')
        crawl_text(f'{green('$ Action:')} get flashlight', 0.10)
        handle_action(self, ACT_GET, item_flashlight.name)
        crawl_text(purple('Your name is engraved on the handle: '
                          f'{red(self.player.name.upper())}'), 0.05)
        crawl_text(purple('The lens is sticky with blood. '
                          'Did someone knock you out '
                          'with your own flashlight?'), 0.05)
        handle_action(self, ACT_GO, 'NORTH')

    def game_over(self):
        crawl_text(red('Your mind feels electric.'), 0.05)
        crawl_text(red('The taste of copper fills your mouth..'), 0.05)
        crawl_text(red('You wonder...'), 0.05)
        crawl_text(purple('\t\t\'Is this real?'), 0.07)
        crawl_text(purple('Am I dreaming this moment?\''), 0.10)
        sys.exit()

    def rubber_duck_death(self):
        crawl_text(f'{red('You hear a faint growl growing louder. '
                          'As you turn to ')}'
                   f'{purple(ACT_LOOK)} '
                   f'{red('you see death in the eye of the beast. '
                          'The growl explodes into a ')}'
                   f'{purple('*BARK*')} '
                   f'{red('You fall to the ground, '
                          'pressed into the mud by the weight of a giant dog. '
                          'The pain is terrible. '
                          'Like sandpaper in your skull. '
                          'You faintly remember two words from a past life: ')}', 0.03)
        crawl_text(purple('King Corso.'), 0.03)
        self.game_over()
