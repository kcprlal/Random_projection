# from random_projection_project import random_projection
# from sklearn.random_projection import GaussianRandomProjection, SparseRandomProjection
# import random

    
# def generate_matrix(n, m):
#     return [[random.randint(0, 9) for _ in range(m)] for _ in range(n)]

# if __name__ == "__main__":
#     rp = random_projection.RandomProjection()
#     X = generate_matrix(3,3)
#     print(X)
#     k = 2  #reduction from X to k

#     Xp = rp.gaussian_random_projection(X, k)
#     Xs = rp.sparse_random_projection(X, k)
#     error = rp.evaluate_distortion(X, Xp)
#     print("avg error:", error)

#     print("\nGAUSSX' =")
#     for row in Xp:
#         print(row)

#     error = rp.evaluate_distortion(X, Xs)
#     print("avg error:", error)

#     print("\nSPARSE X' =")
#     for row in Xs:
#         print(row)

#     # scikit gauss
#     grp = GaussianRandomProjection(n_components=k)
#     X_grp = grp.fit_transform(X)

#     # scikit sparse
#     srp = SparseRandomProjection(n_components=k)
#     X_srp = srp.fit_transform(X)
#     error = rp.evaluate_distortion(X, X_grp)
#     print("avg error:", error)
#     print(f"\nSCIKIT GAUSS:\n{X_grp}")
#     error = rp.evaluate_distortion(X, X_srp)
#     print("avg error:", error)
#     print(f"\nSCIKIT SPARSE:\n{X_srp}")