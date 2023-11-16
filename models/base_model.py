import torch.nn as nn
import torch.nn.functional as F

# network input_size is number of features in dataset
# output_size is number of outputs or possible classifications
class Network(nn.Module):
    def __init__(self, input_size, output_size):
        super(Network, self).__init__()

        # simple model with 3 linear layers and 2 activation functions

        self.layer1 = nn.Linear(input_size, 36)
        self.layer2 = nn.Linear(36, 36)
        self.layer3 = nn.Linear(36, output_size)

    def forward(self, x):
        x1 = F.relu(self.layer1(x))
        x2 = F.relu(self.layer2(x1))
        x3 = self.layer3(x2)
        return x3
