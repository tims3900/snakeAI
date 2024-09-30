import random

class game:
    def __init__(self, width=10, height=10):
        self.width = width
        self.height = height
        self.reset()

    def reset(self):
        self.snake = [(self.width//2, self.height//2)] 
        self.direction = (0, 1)
        self.place_food()
        self.since_last = 0
        self.game_over = False

    def place_food(self):
        while True:
            self.food = (random.randint(0, self.width- 1), 
                         random.randint(0, self.height- 1))
            if self.food not in self.snake:
                break

    def lost(self, head):
        if (head[0] < 0 or head[0] >= self.width or
            head[1] < 0 or head[1] >= self.height or
            head in self.snake):
            return True
        return False

    def get_view(self):
        head_x, head_y = self.snake[0]
        vision = []
        
        # check all 4 directions
        # left, right, up, down
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for dx, dy in directions:
            to_wall, to_food, to_self = 0, 0, 0
            x, y = head_x + dx, head_y + dy
            while 0 <= x < self.width and 0 <= y < self.height:
                to_wall += 1
                if (x, y) == self.food:
                    to_food = to_wall
                if (x, y) in self.snake[1:]:
                    if not to_self:
                        to_self = to_wall    
                x += dx
                y += dy

            vision.extend([1/to_wall if to_wall else 0,
                           1/to_food if to_food else 0,
                           1/to_self if to_self else 0])
        return vision

    def step(self, action):
        # 0 = up
        # 1 = down
        # 2 = left
        # 3 = right
        if action == 0: 
            self.direction = (0, -1)
        elif action == 1:
            self.direction = (0, 1)
        elif action == 2:
            self.direction = (-1, 0)
        elif action == 3:
            self.direction = (1, 0)

        new_head = (self.snake[0][0] + self.direction[0],
                    self.snake[0][1] + self.direction[1])
        
        if self.lost(new_head):
            self.game_over = True
            return -5

        self.snake.insert(0, new_head)

        if new_head == self.food:
            self.place_food()
            self.since_last = 0
            return 5
        else:
            self.snake.pop()
            self.since_last += 1

        # prevent starving
        if self.since_last > self.height * 10:
            self.game_over = True
            return -10

        return 0
