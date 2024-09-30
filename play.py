from blessed import Terminal
from functools import partial

from snake import game

echo = partial(print, end='', flush=True)

def grid(m, n, OFFSET):
    OFFSET -= (n // 2)
    grid_str = ' ' * OFFSET + '┌' + '─' * n + '┐\n'
    for i in range(m):
        grid_str += ' ' * OFFSET + '│' + ' ' * n + '│\n'
    grid_str += ' ' * OFFSET + '└' + '─' * n + '┘\n'
    return grid_str

def action(term, inp, snake):                                                         
    return {term.KEY_UP: 0,
            term.KEY_DOWN: 1,                                                   
            term.KEY_LEFT: 2,                                                   
            term.KEY_RIGHT: 3}.get(inp,                                         
                {(0, -1): 0,                                                    
                 (0, 1): 1,                                                     
                 (-1, 0): 2,                                                    
                 (1, 0): 3}[snake.direction])

def render():
    term = Terminal()
    WIDTH, HEIGHT = term.width, term.height
    grid_width, grid_height = 50, 50

    color_bg = term.on_black
    color_food = term.on_green

    echo(term.move_yx(1, 1))
    echo(color_bg(term.clear))

    snake = game(grid_width, grid_height)
    
    # Calculate horizontal and vertical offsets
    h = (WIDTH - (grid_width + 2)) // 2
    v = (HEIGHT - (grid_height + 2)) // 2

    # Create the grid and adjust it with offsets
    grid_str = grid(grid_height, grid_width, h)

    speed = 0.1
    inp = None
    
    echo(term.move_yx(v , 0))
    echo(color_bg(grid_str))
    echo(term.move_yx(v, 0))
    with term.hidden_cursor(), term.cbreak(), term.location():
        while inp not in (u'q', u'Q'):
            if snake.since_last == 0:
                x_food, y_food = snake.food
                echo(term.move_yx(y_food + v, x_food + h))
                echo(color_food(u' '))

            x_head, y_head = snake.snake[0]
            x_tail, y_tail = snake.snake[-1]
            echo(term.move_yx(y_head + v, x_head + h))
            echo(term.on_blue(u' '))
            inp = term.inkey(timeout=speed)
            next_step = action(term, inp.code, snake)
            if snake.game_over:
                return
            snake.step(next_step)
            # remove the prev tail
            echo(term.move_yx(y_tail + v, x_tail + h))
            echo(color_bg(u' '))
render()
