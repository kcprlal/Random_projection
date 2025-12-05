# Random_projection
> RANDOM PROJECTION Programmer:Kacper Lalik
>
> Tester: Hubert Gąsior

Introduction

The Random Projection algorithm is a technique forreducing the number of
dimensions in a dataset by projectingthe datainto a lower-dimensional
space. The new coordinates of the points are generated randomly, yet
despite this randomness, the algorithm approximately preserves the
distances between points. This means that the overall structure of the
data is largely maintained, while the size of the dataset is reduced and
computations become faster.

Methods in package

> euclidean_distance(self, x, y)
>
> Method calculatesEuclidiandistance between two vectors x, y and
> returns value.This measures how far apart two points are in the
> original or projected space.
>
> Parameters:
>
> x, y–list of numerical values, two vectors
>
> distance_matrix(self, X):
>
> Methodcomputes distance between two points in a matrix. It only
> computesthe upper triangle ofthe matrix, then mirrors it to the
> lowertriangle (because distance is symmetric).
>
> Parameters:
>
> X –list\[list\]of numerical values, matrixof which distance matrix is
> made
>
> evaluate_distortion(self, X_original, X_projected)
>
> Method calculate relativeerror between two points in original and
> projected matrix. After all calculations sums it up and returns
> average relative error which occurredby transforming points.
>
> Parameters:
>
> X_original-list\[list\]of numerical values, matrix to perform
> projection on
>
> X_projected-list\[list\]of numerical values, matrix afterprojection
>
> scale_matrix(self, R, k)
>
> Method scales randomprojection matrix Rto preserve distances
> approximately after projection by dividingall elements by sqrt(k)
>
> Parameters:
>
> R –list\[list\] of numerical values, matrix with distributed values
>
> k -numerical value,numberof dimensions
>
> gaussian_random_projection(self, X,k)
>
> Method performs gaussian random projection by creatingrandom gaussian
> matrix(R)len(X) x k with values between 0, 1, scaling withmethod
> scale_matrix(),multiplyingeach data pointof matrix X by matrix R to
> get its projection in k dimensions.
>
> Parameters:
>
> X –list\[list\] of numerical values, matrix to perform projection on
>
> k–numerical value,expected dimensions after projection
>
> sparse_random_projection(self, X, k, s=3)
>
> Methhod performs sparse random projection by creatingmartrix (R)
> whichcontains only 0 and +-1determined randomly by s parameter with
> probability1/s. After thatperformssame operations as
> gaussian_random_projection
>
> Parameters:
>
> X –list\[list\] of numerical values, matrix to perform projection on
>
> k–numerical value,expected dimensions after projection
>
> s –numerical value, propability 1/s for+-value in matrix R

Tests

> test_euclidean_distance()
>
> Checks that the Euclidean distance between two points is calculated
> correctly.
>
> test_distance_matrix_symmetry()
>
> Verifies that the distance matrix is symmetric and all diagonal
> elements are zero.
>
> test_evaluate_distortion_zero_for_identical_matrices()
>
> Ensures that the distortion evaluation returns zero when the original
> and projected matrices are identical.
>
> test_scale_matrix_scales_correctly()
>
> Confirmsthatthe scaling function multiplies each element of the matrix
> by the correct factor.
>
> test_gaussian_random_projection_shape()
>
> Checks that Gaussian random projection produces a projected dataset
> with the correct number of rows and columns.
>
> test_sparse_random_projection_shape()
>
> Checks that sparse random projection produces a projected dataset with
> the correct number of rows and columns.
>
> test_gaussian_random_projection_large_vs_sklearn()
>
> Checks that the custom Gaussian random projection produces a projected
> dataset withthe same shape as scikit-learn’s implementation and that
> the average pairwise distances are within 10%of each other.
>
> test_sparse_random_projection_large_vs_sklearn()
>
> Checks that the custom sparse random projection produces a projected
> dataset withthe same shape as scikit-learn’s sparse implementationand
> that the average pairwise distances are within 40%of each other.

Way of work

> 1\. Importlibraryrandom_projection 2. Create object RandomProjection
>
> 3\. Performgaussian_random_projection(X,
> k)orsparse_random_projection(X, k)on matrix
>
> 4\. Optionally perform evaluate_distortion(X1,X2)to evaluate error
