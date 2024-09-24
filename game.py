import sys
import time
from textwrap import wrap
from actions import ACT_GET, ACT_GO, ACT_LOOK, handle_action
from color import purple, red
from item import item_toy


def crawl_text(text, delay=0.01):
    text = wrap(text, 50)
    text = '\n\r'.join(text)
    for ln in text:
        print(ln, end='', flush=True)
        time.sleep(delay)
    print('\n')


class Game:
    def __init__(self, player):
        self.player = player

    def game_start(self):
        crawl_text('\n')
        crawl_text('You awaken suddenly.')
        handle_action(self, ACT_LOOK, '')
        handle_action(self, ACT_GET, 'FLASHLIGHT')
        crawl_text(purple('It is wet with blood.'), 0.02)
        crawl_text(purple('Did someone knock you out '
                          'with your own flashlight?'), 0.02)
        crawl_text(purple('You can see your name engraved on the handle:'), 0.02)
        crawl_text(red(self.player.name.upper()), 0.02)
        handle_action(self, ACT_GO, 'NORTH')

    def game_over(self):
        crawl_text('\n\f\t\t')
        crawl_text(f'{red('Your mind feels electric, '
                          'the taste of copper fills your mouth, '
                          'and you wonder:')}')
        crawl_text(
            f'{purple('Is this real? Am I dreaming this moment?')}')
        crawl_text('\n\f\t\t')
        sys.exit()

    def rubber_duck_death(self):
        crawl_text(f'{purple(item_toy.desc)}', 0.03)
        crawl_text(f'{red('You hear a faint growl growing louder. '
                          'As you turn to ')}'
                   f'{purple('look ')}'
                   f'{red('you see death in the eye of the beast. '
                          'The growl explodes into a bark. '
                          'You fall to the ground, '
                          'pressed into the mud by the weight of a giant dog. '
                          'The pain is terrible, '
                          'it feels like sandpaper on your skull, '
                          'and you faintly remember two words from a past life: ')}' +
                   f'{purple('King Corso.')}', 0.03)
        self.game_over()
