from .cluster_dataset import ClusterDataset
from .cluster_det_processor import ClusterDetProcessor
from .build_dataloader import build_dataloader


__factory = {
     'det': ClusterDetProcessor,
}


def build_dataset(cfg):
    return ClusterDataset(cfg)


def build_processor(name):
    if name not in __factory:
        raise KeyError("Unknown processor:", name)
    return __factory[name]
