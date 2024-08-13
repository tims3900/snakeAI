from blessed import Terminal
from functools import partial

echo = partial(print, end = '', flush=True)

def grid(m, n, OFFSET):
    OFFSET -= (n // 2)
    grid_str = ' ' * OFFSET + '┌' + '─' * n + '┐\n'
    for i in range(m):
        grid_str += ' ' * OFFSET + '│' + ' ' * n + '│\n'
    grid_str += ' ' * OFFSET + '└' + '─' * n + '┘\n'
    return grid_str

def head(direction):
    return u':'

def render():
    term = Terminal()
    WIDTH, HEIGHT = term.width, term.height
    color_nibble = term.black_on_green
    color_worm = term.yellow_reverse
    color_head = term.red_reverse

    grid_width, grid_height = 50, 50

    # Calculate horizontal and vertical offsets
    horizontal_offset = (WIDTH - (grid_width + 2)) // 2
    vertical_offset = (HEIGHT - (grid_height + 2)) // 2

    # Create the grid and adjust it with offsets
    grid_str = grid(grid_height, grid_width, horizontal_offset)
    centered_grid = term.move_yx(vertical_offset, 0) + grid_str

    echo(term.move_yx(1, 1))
    echo(term.clear)

    speed = 0.1
    inp = None

    echo(centered_grid)
    echo(term.move_yx(HEIGHT, 0))
    with term.hidden_cursor(), term.cbreak(), term.location():
        while inp not in (u'q', u'Q'):
            echo(term.move_yx(HEIGHT // 2, horizontal_offset) + color_head(head(0)))
            inp = term.inkey(timeout=speed)

render()
