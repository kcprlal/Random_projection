from sklearn.random_projection import GaussianRandomProjection, SparseRandomProjection
import random
import math

def euclidean_distance(x, y):
    return math.sqrt(sum((x[i] - y[i]) ** 2 for i in range(len(x))))

def evaluate_distortion(X_original, X_projected):
    D1 = distance_matrix(X_original)
    D2 = distance_matrix(X_projected)
    n = len(D1)
    errors = []
    for i in range(n):
        for j in range(i + 1, n):
            if D1[i][j] > 0:
                rel_error = abs(D1[i][j] - D2[i][j]) / D1[i][j]
                errors.append(rel_error)

    if len(errors) == 0:
        return 0.0

    return sum(errors) / len(errors)


def distance_matrix(X):
    n = len(X)
    D = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(i + 1, n):
            d = euclidean_distance(X[i], X[j])
            D[i][j] = d
            D[j][i] = d

    return D

def generate_matrix(n, m):
    return [[random.randint(0, 9) for _ in range(m)] for _ in range(n)]

def scale_matrix(d, R):
    scale = 1.0 / math.sqrt(k)
    for i in range(d):
        for j in range(k):
            R[i][j] *= scale
    return R
def gaussian_random_projection(X, k):
    d = len(X[0])
    #gaussian matrix
    R = [[random.gauss(0, 1) for _ in range(k)] for _ in range(d)]
    # scale 1/sqrt(k)
    R = scale_matrix(d, R)
    # calculate X' = X * R (n x k)
    X_proj = []
    for row in X:
        projected_row = []
        for j in range(k):
            s = 0.0
            for i in range(d):
                s += row[i] * R[i][j]
            projected_row.append(s)
        X_proj.append(projected_row)

    return X_proj

def sparse_random_projection(X, k, s=3):
    n = len(X)
    d = len(X[0])

    R = [[0 for _ in range(k)] for _ in range(d)]

    for i in range(d):
        for j in range(k):
            r = random.random()
            if r < 1/(2*s):
                R[i][j] = 1
            elif r < 1/(2*s) + 1/(2*s):
                R[i][j] = -1
            # else: R[i][j] remains 0 (sparse)

    R = scale_matrix(d, R)

    # project
    X_proj = []
    for row in X:
        projected_row = []
        for j in range(k):
            s_val = 0.0
            for i in range(d):
                if R[i][j] != 0: #skip 0 to speedup
                    s_val += row[i] * R[i][j]
            projected_row.append(s_val)
        X_proj.append(projected_row)

    return X_proj

if __name__ == "__main__":
    X = generate_matrix(3,3)
    print(X)
    k = 2  #reduction from X to k

    Xp = gaussian_random_projection(X, k)
    Xs = sparse_random_projection(X, k)
    error = evaluate_distortion(X, Xp)
    print("Średni błąd dystansu:", error)

    print("\nGAUSSX' =")
    for row in Xp:
        print(row)

    error = evaluate_distortion(X, Xs)
    print("Średni błąd dystansu:", error)

    print("\nSPARSE X' =")
    for row in Xs:
        print(row)

    # scikit gauss
    grp = GaussianRandomProjection(n_components=k)
    X_grp = grp.fit_transform(X)

    # scikit sparse
    srp = SparseRandomProjection(n_components=k)
    X_srp = srp.fit_transform(X)
    error = evaluate_distortion(X, X_grp)
    print("Średni błąd dystansu:", error)
    print(f"\nSCIKIT GAUSS:\n{X_grp}")
    error = evaluate_distortion(X, X_srp)
    print("Średni błąd dystansu:", error)
    print(f"\nSCIKIT SPARSE:\n{X_srp}")