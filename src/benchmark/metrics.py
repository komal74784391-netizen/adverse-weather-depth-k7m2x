import numpy as np


def abs_rel(pred, gt):
    valid = gt > 0
    return float(np.mean(np.abs(pred[valid] - gt[valid]) / gt[valid]))


def rmse(pred, gt):
    return float(np.sqrt(np.mean((pred - gt) ** 2)))
