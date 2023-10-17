import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
import collections
from collections import OrderedDict as od

layer1 = nn.Sequential(
    od(
        [
            ("conv1", nn.Conv2d(3, 64, 3)),
            ("bn1", nn.BatchNorm2d(64)),
            (
                "res1",
                nn.Sequential(
                    od([("rconv1", nn.Conv2d(64, 128, 3)), ("relu1", nn.ReLU())])
                ),
            ),
        ]
    )
)
