import torch
import torch_geometric.transform as T
from torch_geometric.datasets.dataset import Data


def test_compose():
    transform = T.Compose([T.Cartesian(cat=False), T.Cartesian(cat=True)])
    expected_output = ('Compose([\n'
                       '    Cartesian(cat=False),\n'
                       '    Cartesian(cat=True),\n'
                       '])')
    assert transform.__repr__() == expected_output

    pos = torch.Tensor([[-1, 0], [0, 0], [2, 0]])
    edge_index = torch.LongTensor([[0, 1], [1, 2]])
    data = Data(None, pos, edge_index, None, None)
    expected_output = [[0.75, 0.5, 0.75, 0.5], [1, 0.5, 1, 0.5]]

    output = transform(data)
    assert output.weight.tolist() == expected_output