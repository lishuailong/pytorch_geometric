import math

import torch
from torch.nn import Module, Parameter

from torch_geometric.nn.functional import gcn


class GCN(Module):
    """
    Args:
        in_features (int): Size of each input sample.
        out_features (int): Size of each output sample.
        bias (bool, optional): If set to False, the layer will not learn an
            additive bias. Default: `True`.
    """

    def __init__(self, in_features, out_features, bias=True):
        super(GCN, self).__init__()

        self.in_features = in_features
        self.out_features = out_features
        self.weight = Parameter(torch.Tensor(in_features, out_features))

        if bias:
            self.bias = Parameter(torch.Tensor(out_features))
        else:
            self.register_parameter('bias', None)

        self.reset_parameters()

    def reset_parameters(self):
        stdv = 1. / math.sqrt(self.in_channels)

        self.weight.data.uniform_(-stdv, stdv)
        if self.bias is not None:
            self.bias.data.uniform_(-stdv, stdv)

    def forward(self, adj, features):
        return gcn(adj, features, self.weight, self.bias)

    def __repr__(self):
        s = ('{name}({in_channels}, {out_channels}')
        if self.bias is None:
            s += 'bias=False'
        s += ')'
        return s.format(name=self.__class__.__name__, **self.__dict__)