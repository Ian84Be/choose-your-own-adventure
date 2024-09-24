from textwrap import wrap
from color import red, purple


class Object:
    def __init__(self, name, desc='N/A'):
        desc = wrap(desc, 50)
        self.name = name
        self.desc = '\n'.join(desc)

    def __str__(self):
        return f'{red(self.name)}\n{purple(self.desc)}'
