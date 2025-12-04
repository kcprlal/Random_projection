import pytest
import random
import numpy as np
from random_projection_project.random_projection import RandomProjection
from sklearn.random_projection import GaussianRandomProjection as SKGaussian
from sklearn.random_projection import SparseRandomProjection as SKSparse

def test_gaussian_random_projection_large_vs_sklearn():
    np.random.seed(42)
    X = np.random.rand(100, 50)
    k = 10

    rp = RandomProjection()
    X_proj_custom = rp.gaussian_random_projection(X.tolist(), k)

    sk_rp = SKGaussian(n_components=k, random_state=42)
    X_proj_sklearn = sk_rp.fit_transform(X)

    assert np.shape(X_proj_custom) == np.shape(X_proj_sklearn)

    def mean_pairwise_distance(mat):
        n = len(mat)
        total = 0.0
        count = 0
        for i in range(n):
            for j in range(i+1, n):
                total += np.linalg.norm(np.array(mat[i]) - np.array(mat[j]))
                count += 1
        return total / count

    d_custom = mean_pairwise_distance(X_proj_custom)
    d_sklearn = mean_pairwise_distance(X_proj_sklearn)

    rel_error = abs(d_custom - d_sklearn) / d_sklearn
    assert rel_error < 0.10


def test_sparse_random_projection_large_vs_sklearn():
    np.random.seed(42)
    random.seed(42)
    X = np.random.rand(100, 50)
    k = 10

    rp = RandomProjection()
    X_proj_custom = rp.sparse_random_projection(X.tolist(), k, s=3)

    sk_rp = SKSparse(n_components=k, density=1/3, random_state=42)
    X_proj_sklearn = sk_rp.fit_transform(X)

    assert np.shape(X_proj_custom) == np.shape(X_proj_sklearn)

    def mean_pairwise_distance(mat):
        n = len(mat)
        total = 0.0
        count = 0
        for i in range(n):
            for j in range(i+1, n):
                total += np.linalg.norm(np.array(mat[i]) - np.array(mat[j]))
                count += 1
        return total / count

    d_custom = mean_pairwise_distance(X_proj_custom)
    d_sklearn = mean_pairwise_distance(X_proj_sklearn)

    rel_error = abs(d_custom - d_sklearn) / d_sklearn
    assert rel_error < 0.4
