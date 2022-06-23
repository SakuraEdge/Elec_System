import torch
import torch.nn as nn


class Net(nn.Module):
    def __init__(self, hidden_size):
        super(Net, self).__init__()
        self.feature = nn.Sequential(
            nn.Linear(2, hidden_size),
            nn.ReLU(),
            nn.Linear(hidden_size, hidden_size),
            nn.ReLU(),
            nn.Linear(hidden_size, hidden_size),
            nn.ReLU(),
        )
        self.classfier = nn.Sequential(
            nn.Linear(hidden_size, 3),
        )
    
    def forward(self, x):
        x = self.feature(x)
        x = self.classfier(x)
        return x
