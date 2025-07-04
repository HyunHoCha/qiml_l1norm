import numpy as np
import math


def SIGMA_F_SQUARED(is_gaussian):
    return 1 if is_gaussian else 1 / 3


def random_A(m, n, is_gaussian):
    return np.random.randn(m, n) if is_gaussian else np.random.uniform(-1, 1, size=(m, n))


def random_x(n, is_gaussian):
    return np.random.randn(n, 1) if is_gaussian else np.random.uniform(-1, 1, size=(n, 1))
