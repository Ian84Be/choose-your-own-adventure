ascii_color = {
    'PURPLE': '\033[95m',
    'CYAN': '\033[96m',
    'DARKCYAN': '\033[36m',
    'BLUE': '\033[94m',
    'GREEN': '\033[92m',
    'YELLOW': '\033[93m',
    'RED': '\033[91m',
    'BOLD': '\033[1m',
    'UNDERLINE': '\033[4m',
    'END': '\033[0m',
}


def color_string(color, string):
    return f'{color}{string}{ascii_color.get('END')}'


def purple(string):
    return color_string(ascii_color.get('PURPLE'), string)


def green(string):
    return color_string(ascii_color.get('GREEN'), string)


def red(string):
    return color_string(ascii_color.get('RED'), string)


def bold(string):
    return color_string(ascii_color.get('BOLD'), string)
