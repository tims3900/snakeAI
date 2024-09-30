from snake import game

def print_state(game):
    print(f"Snake: {game.snake}")
    print(f"Food: {game.food}")
    print(f"Game Over: {game.game_over}")
    print("-" * 20)

def test_snake_game():
    test = game(grid_size=10)

    print("Initial State")
    print_state(test)

    test.food = (5, 7)

    actions = [3, 3, 1, 1, 2, 2, 0, 0]  # right, right, down, down, left, left, up, up
    for step, action in enumerate(actions):
        if test.game_over:
            break
        reward = test.step(action)
        print(f"Step {step + 1}, Action: {action}, Reward: {reward}")
        print_state(test)

if __name__ == "__main__":
    test_snake_game()
