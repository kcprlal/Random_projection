import math
import random

class RandomProjection:
    def __init__(self):
        pass

    def euclidean_distance(self, x, y):
        return math.sqrt(sum((x[i] - y[i]) ** 2 for i in range(len(x))))

    def distance_matrix(self, X):
        n = len(X)
        D = [[0 for _ in range(n)] for _ in range(n)]

        for i in range(n):
            for j in range(i + 1, n):
                d = self.euclidean_distance(X[i], X[j])
                D[i][j] = d
                D[j][i] = d

        return D

    def evaluate_distortion(self, X_original, X_projected):
        D1 = self.distance_matrix(X_original)
        D2 = self.distance_matrix(X_projected)
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

    def scale_matrix(self, R, k):
        scale = 1.0 / math.sqrt(k)
        d = len(R)

        for i in range(d):
            for j in range(len(R[0])):
                R[i][j] *= scale

        return R

    def gaussian_random_projection(self, X, k):
        d = len(X[0])

        R = [[random.gauss(0, 1) for _ in range(k)] for _ in range(d)]

        R = self.scale_matrix(R, k)

        X_proj = []
        for row in X:
            projected_row = []
            for j in range(k):
                s = sum(row[i] * R[i][j] for i in range(d))
                projected_row.append(s)
            X_proj.append(projected_row)

        return X_proj

    def sparse_random_projection(self, X, k, s=3):
        d = len(X[0])

        R = [[0 for _ in range(k)] for _ in range(d)]

        for i in range(d):
            for j in range(k):
                r = random.random()
                if r < 1/(2*s):
                    R[i][j] = 1
                elif r < 1/s:
                    R[i][j] = -1

        R = self.scale_matrix(R, k)

        X_proj = []
        for row in X:
            projected_row = []
            for j in range(k):
                s_val = 0.0
                for i in range(d):
                    if R[i][j] != 0:
                        s_val += row[i] * R[i][j]
                projected_row.append(s_val)
            X_proj.append(projected_row)

        return X_proj
