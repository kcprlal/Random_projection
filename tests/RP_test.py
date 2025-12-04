# tests/test_random_projection.py
import math
import pytest
from random_projection_project.random_projection import RandomProjection

def test_euclidean_distance():
    rp = RandomProjection()
    x = [0, 0]
    y = [3, 4]
    assert rp.euclidean_distance(x, y) == 5.0 

def test_distance_matrix_symmetry():
    rp = RandomProjection()
    X = [[0, 0], [3, 4], [6, 8]]
    D = rp.distance_matrix(X)
    n = len(D)
    for i in range(n):
        for j in range(n):
            assert D[i][j] == D[j][i]
        assert D[i][i] == 0

def test_evaluate_distortion_zero_for_identical_matrices():
    rp = RandomProjection()
    X = [[1, 2], [3, 4]]
    assert rp.evaluate_distortion(X, X) == 0.0

def test_scale_matrix_scales_correctly():
    rp = RandomProjection()
    R = [[1, 2], [3, 4]]
    k = 2
    R_scaled = rp.scale_matrix(R, k)
    scale = 1 / math.sqrt(k)
    expected = [[1*scale, 2*scale], [3*scale, 4*scale]]
    for i in range(len(R)):
        for j in range(len(R[0])):
            assert math.isclose(R_scaled[i][j], expected[i][j], rel_tol=1e-9)

def test_gaussian_random_projection_shape():
    rp = RandomProjection()
    X = [[1, 2], [3, 4], [5, 6]]
    k = 2
    X_proj = rp.gaussian_random_projection(X, k)
    assert len(X_proj) == len(X)
    assert all(len(row) == k for row in X_proj)

def test_sparse_random_projection_shape():
    rp = RandomProjection()
    X = [[1, 2], [3, 4]]
    k = 3
    X_proj = rp.sparse_random_projection(X, k)
    assert len(X_proj) == len(X)
    assert all(len(row) == k for row in X_proj)

