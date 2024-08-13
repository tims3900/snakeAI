import torch
import torch.nn as nn
import torch.nn.functional as F

class snakeNN(nn.Module):
    def __init__(self):
        super(snakeNN, self).__init__()

        self.a = nn.Linear(12, 64) # Input to Hidden
        self.b = nn.Linear(64, 64) # Hidden to Hidden
        self.c = nn.Linear(64, 4)  # Hidden to Output

    def forward(self, x):
        x = F.relu(self.a(x))
        x = F.relu(self.b(x))
        x = self.c(x)
        return x
