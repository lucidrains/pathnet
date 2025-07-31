import torch
from torch.nn import Module, ModuleList

# helpers

def exists(v):
    return v is not None

def default(v, d):
    return v if exists(v) else d

# class

class Pathnet(Module):
    def __init__(
        self
    ):
        super().__init__()
