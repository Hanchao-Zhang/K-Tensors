
class ClusteringCPC:
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
