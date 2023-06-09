# K-Tensors: 

K-Tensors is a clustering algorithm for positive semi-definite matrices that 

` ClusteringCPC(Psis, K, max_iter=1000).clustering()`

Psis: a 3D array of size (n, p, p) where n is the number of matrices and p is the dimension of the positive semi-definite matrices.
K: number of clusters
max_iter: maximum number of iterations, default is 1000, usually finish within 10 iterations

return:
- group1: a vector of length n, each element is an index of group membership
- centers0_cpcs: K orthonormal basis matrices of size p by p for each cluster
- F: $\mathbf F = \mathbf B^\top \mathbf\Psi \mathbf B$
- diagF: $\mathbf F = (\mathbf B^\top \mathbf\Psi \mathbf B) \circ \mathbf I$ the diagonal of matrix $\mathbf F$
- centers0: Mean of each cluster
- mse_vec: loss function for each iteration