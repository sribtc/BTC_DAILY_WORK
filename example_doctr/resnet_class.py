import torch
import torch.nn as nn
import torch.nn.functional as F


class BasicBlock(nn.Module):
    def __init__(self, inplanes, planes, strdie=1) -> None:
        super(BasicBlock, self).__init__()

        self.conv1 = nn.Conv2d(
            inplanes, planes, kernel_size=3, stride=strdie, padding=1, bias=False
        )

        self.bn1 = nn.BatchNorm2d(planes)

        self.conv2 = nn.Conv2d(
            planes, planes, kernel_size=3, stride=1, padding=1, bias=False
        )

        self.bn2 = nn.BatchNorm2d(planes)
        self.shortcut = nn.Sequential()

    def forward(self, x):
        out = F.relu(self.bn1(self.conv1(x)))
        out = F.relu(self.bn2(self.conv2(out)))
        out += self.shortcut(x)
        out = F.relu(out)
        return out


class CustomBlock(nn.Module):
    def __init__(self, in_channels, out_channels) -> None:
        super(CustomBlock, self).__init__()

        self.inner_layer = nn.Sequential(
            nn.Conv2d(
                in_channels=in_channels,
                out_channels=out_channels,
                stride=1,
                kernel_size=3,
                padding=1,
                bias=False,
            ),
            nn.MaxPool2d(2),
            nn.BatchNorm2d(out_channels),
            nn.ReLU(),
        )

        self.res_block = BasicBlock(out_channels, out_channels)

    def forward(self, x):
        x = self.inner_layer(x)
        r = self.res_block(x)
        out = x + r
        return out
