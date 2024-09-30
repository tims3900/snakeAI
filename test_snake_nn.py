import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
from nn_snake import snakeNN
from snake import game

# Initialize the game and neural network
game_instance = game(grid_size=10)
model = snakeNN()

# Set the model to training mode
model.train()

# Define the optimizer and loss function
optimizer = optim.Adam(model.parameters(), lr=0.001)
criterion = nn.MSELoss()

def train_model(epochs):
    for epoch in range(epochs):
        game_instance.reset()
        total_loss = 0
        
        while not game_instance.game_over:
            state = torch.tensor(game_instance.get_view(), dtype=torch.float32).unsqueeze(0)
            
            # Forward pass
            action_scores = model(state)
            
            # Choose the action with the highest score
            action = torch.argmax(action_scores).item()
            
            # Take the action in the game and get the reward
            reward = game_instance.step(action)
            
            # Create a target tensor for the loss calculation
            target = torch.tensor([reward], dtype=torch.float32)
            
            # Compute the loss
            loss = criterion(action_scores[0, action], target)
            
            # Zero gradients, backward pass, optimizer step
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            
            total_loss += loss.item()
        
        print(f"Epoch {epoch + 1}/{epochs}, Loss: {total_loss}")

# Train the model
train_model(epochs=500)
