# Random Projection

## Introduction

### Developer: Kacper Lalik
### Tester: Hubert Gąsior

The **Random Projection** algorithm is a technique for reducing the number of dimensions in a dataset by projecting the data into a lower-dimensional space. The new coordinates of the points are generated randomly; however, despite this randomness, the algorithm approximately preserves the distances between points.

As a result, the overall structure of the data is largely maintained while the dataset size is reduced and computations become faster.

---

## Methods in the Package

### `euclidean_distance(self, x, y)`

Calculates the **Euclidean distance** between two vectors `x` and `y`.

This method measures how far apart two points are in the original or projected space.

**Parameters:**

* `x` – list of numerical values (vector)
* `y` – list of numerical values (vector)

**Returns:**

* Numerical value representing the Euclidean distance

---

### `distance_matrix(self, X)`

Computes the distance matrix for a given dataset.

The method calculates distances only for the upper triangle of the matrix and mirrors it to the lower triangle (since distance is symmetric).

**Parameters:**

* `X` – list of lists of numerical values (input matrix)

**Returns:**

* Symmetric distance matrix

---

### `evaluate_distortion(self, X_original, X_projected)`

Calculates the **average relative error** between distances in the original space and the projected space.

The method sums all relative errors and returns their average, representing the distortion introduced by the projection.

**Parameters:**

* `X_original` – list of lists of numerical values (original data matrix)
* `X_projected` – list of lists of numerical values (projected data matrix)

**Returns:**

* Average relative error

---

### `scale_matrix(self, R, k)`

Scales the random projection matrix `R` to approximately preserve distances after projection.

Each element of the matrix is divided by `√k`.

**Parameters:**

* `R` – list of lists of numerical values (random projection matrix)
* `k` – integer, number of target dimensions

**Returns:**

* Scaled projection matrix

---

### `gaussian_random_projection(self, X, k)`

Performs **Gaussian Random Projection**.

A random Gaussian matrix `R` of shape `(len(X), k)` with values drawn from a normal distribution is created and scaled using `scale_matrix()`. Each data point in `X` is then multiplied by `R` to obtain its projection into `k` dimensions.

**Parameters:**

* `X` – list of lists of numerical values (input data matrix)
* `k` – integer, target number of dimensions

**Returns:**

* Projected dataset

---

### `sparse_random_projection(self, X, k, s=3)`

Performs **Sparse Random Projection**.

A sparse random matrix `R` is created, containing only values `0` and `±1`. The probability of a non-zero value is `1 / s`. The remaining steps are the same as in `gaussian_random_projection`.

**Parameters:**

* `X` – list of lists of numerical values (input data matrix)
* `k` – integer, target number of dimensions
* `s` – integer, controls sparsity (probability `1 / s` for non-zero entries)

**Returns:**

* Projected dataset

---

## Tests

### `test_euclidean_distance()`

Checks that the Euclidean distance between two points is calculated correctly.

### `test_distance_matrix_symmetry()`

Verifies that the distance matrix is symmetric and that all diagonal elements are zero.

### `test_evaluate_distortion_zero_for_identical_matrices()`

Ensures that the distortion evaluation returns zero when the original and projected matrices are identical.

### `test_scale_matrix_scales_correctly()`

Confirms that the scaling function divides each element of the matrix by the correct factor.

### `test_gaussian_random_projection_shape()`

Checks that Gaussian random projection produces a dataset with the correct shape.

### `test_sparse_random_projection_shape()`

Checks that sparse random projection produces a dataset with the correct shape.

### `test_gaussian_random_projection_large_vs_sklearn()`

Verifies that the custom Gaussian random projection:

* Produces a dataset with the same shape as scikit-learn’s implementation
* Preserves average pairwise distances within **10%**

### `test_sparse_random_projection_large_vs_sklearn()`

Verifies that the custom sparse random projection:

* Produces a dataset with the same shape as scikit-learn’s sparse implementation
* Preserves average pairwise distances within **40%**

---

## Workflow

1. Import the library:

   ```python
   import random_projection
   ```
2. Create a `RandomProjection` object
3. Perform projection:

   * `gaussian_random_projection(X, k)` **or**
   * `sparse_random_projection(X, k)`
4. (Optional) Evaluate distortion:

   ```python
   evaluate_distortion(X_original, X_projected)
   ```
