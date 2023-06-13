"""
Perform K-Tensors Clustering Algorithm for Positive Semi-Denfinite Matrices

Parameters:
    Psis (3D np.array): The input matrices to be clustered with shape (n, p, p)
    K (int): The number of clusters
    max_iter (int): The maximum number of iterations

Returns:
    group1 (np.array): The cluster labels for each input matrix
    centers0_cpcs (np.array): The common principal components of the clusters
    F (np.array): The orthonormal transformation of the input matrices to the
        common principal components
    diagF (np.array): The diagonal matrices of the orthonormal transformation
        of the input matrices to the common principal components
    centers0 (np.array): The centers of the clusters
    mse_vec (list): The mean squared error of the clusters at each iteration
"""
import numpy as np
import scipy

class KTensors:
    def __init__(self, Psis, K, max_iter=1000):
        self.Psis = Psis
        self.K = K
        self.n = Psis.shape[0]
        self.p = Psis.shape[1]
        self.max_iter = max_iter

    def clustering(self):
        group0 = np.random.choice(range(self.K), self.n, replace=True)
        group1 = np.random.choice(range(self.K), self.n, replace=True)
        err0 = 4
        err1 = 2
        mse_vec = []
        niter = 0
        while err0 != err1 and niter < self.max_iter:
            niter += 1
            group0 = group1.copy()
            err0 = err1
            index0 = list(map(lambda k: np.where(group0 == k), range(self.K)))

            centers0 = np.array(
                list(map(lambda indxk: self.Psis[indxk, :, :].mean(1), index0)))
            centers0_cpcs = np.array(list(
                map(lambda k: np.linalg.eig(centers0[k, :, :])[1], range(self.K)))).squeeze(1)

            F_center0 = np.array(list(map(lambda k:  list(map(lambda i: centers0_cpcs[k].T.dot(
                self.Psis[i, :, :]).dot(centers0_cpcs[k]), range(self.n))), range(self.K))))
            F_off_norm = np.array(list(map(lambda k:  list(
                map(lambda i:  np.linalg.norm(F_center0[k][i, :, :] - np.diag(np.diag(F_center0[k][i, :, :]))), range(self.n))), range(self.K)))).T

            group1 = np.array(
                list(map(lambda i: F_off_norm[i, :].argmin(), range(self.n))))
            err1 = np.array(
                list(map(lambda i: F_off_norm[i, :].min(), range(self.n)))).mean()
            mse_vec.append(err1)
            # print(niter, err1)

        F_center0.shape
        F = np.array(
            list(map(lambda i: F_center0[group1[i]][i, :, :], range(self.n))))
        diagF = np.array(
            list(map(lambda i: np.diag(F[i, :, :]), range(self.n))))
        centers0 = centers0.squeeze(1)
        return group1, centers0_cpcs, F, diagF, centers0, mse_vec




class Distance:
    def __init__(self, sigma1, sigma2):
        self.sigma1 = sigma1.squeeze()
        self.sigma2 = sigma2.squeeze()

    def euclidean(self):
        return np.linalg.norm(self.sigma1 - self.sigma2)

    def affine_invariant(self):
        # get sqaure root of inverse of sigma1
        eigenvalues, _ = np.linalg.eig(np.linalg.inv(self.sigma1) @ self.sigma2)
        return np.sum(np.log(eigenvalues) ** 2)

    def log_euclidean(self):
        return np.linalg.norm(
            scipy.linalg.logm(self.sigma1) - scipy.linalg.logm(self.sigma2)
        )
    
    def log_det(self):
        return np.trace(np.linalg.inv(self.sigma1) @ self.sigma2 - np.eye(self.sigma1.shape[0])) - np.log(np.linalg.det(np.linalg.inv(self.sigma1) @ self.sigma2))
    
    def symmetric_stein(self):
        return np.log(np.linalg.det((self.sigma1 + self.sigma2) / 2)) - 0.5 * np.log(np.linalg.det(self.sigma1 @ self.sigma2))





class KMetrics:
    def __init__(self, Psis, K, metric):
        self.Psis = Psis
        self.K = K
        self.metric = metric

    def clustering(self):
        n = self.Psis.shape[0]
        mse_vec = []

        group0 = np.random.choice(range(self.K), size=n, replace=True)
        group1 = np.random.choice(range(self.K), size=n, replace=True)

        err0 = 4
        err1 = 2
        niter = 0

        while (err1 != err0):
            err0 = err1
            group0 = group1.copy()
            index0 = list(map(lambda k: np.where(group0 == k), range(self.K)))
            centers0 = np.array(
                list(map(lambda indxk: self.Psis[indxk, :, :].mean(1), index0))
            )

            if self.metric == "euclidean":
                distances0 = np.array(list(map(lambda Psisi: list(map(lambda centersi: Distance(Psisi, centersi).euclidean(), centers0)), self.Psis)))
            elif self.metric == "affine_invariant":
                distances0 = np.array(list(map(lambda Psisi: list(map(lambda centersi: Distance(Psisi, centersi).affine_invariant(), centers0)), self.Psis)))
            elif self.metric == "log_euclidean":
                distances0 = np.array(list(map(lambda Psisi: list(map(lambda centersi: Distance(Psisi, centersi).log_euclidean(), centers0)), self.Psis)))
            elif self.metric == "log_det":
                distances0 = np.array(list(map(lambda Psisi: list(map(lambda centersi: Distance(Psisi, centersi).log_det(), centers0)), self.Psis)))
            elif self.metric == "symmetric_stein":
                distances0 = np.array(list(map(lambda Psisi: list(map(lambda centersi: Distance(Psisi, centersi).symmetric_stein(), centers0)), self.Psis)))

            group1 = distances0.argmin(1)
            err1 = distances0.min(1).mean()
            niter += 1
            mse_vec.append(err1)

        return group1, mse_vec