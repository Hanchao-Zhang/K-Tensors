K-Tensors: Clustering Positive Semi-Definite Matrices<img src="./pic2.png" align="right" width="150" />
========================================================================================================================


[![Project Status:
Active](http://www.repostatus.org/badges/latest/active.svg)](http://www.repostatus.org/#active) [![Build
Status](https://travis-ci.org/stephenslab/clusteringCPC.svg?branch=master)](https://travis-ci.org/stephenslab/clusteringCPC) [![codecov](https://codecov.io/gh/stephenslab/clusteringCPC/branch/master/graph/badge.svg)](https://codecov.io/gh/stephenslab/clusteringCPC) [![CRAN\_Status\_Badge](http://www.r-pkg.org/badges/version/clusteringCPC)](https://cran.r-project.org/package=clusteringCPC) [![CRAN\_Download\_Badge](http://cranlogs.r-pkg.org/badges/clusteringCPC)](https://cran.r-project.org/package=clusteringCPC)



## About the Function


` ClusteringCPC(Psis, K, max_iter=1000).clustering()`

input:
- Psis: a 3D array of size (n, p, p) where n is the number of matrices and p is the dimension of the positive semi-definite matrices.
- K: number of clusters
- max_iter: maximum number of iterations, default is 1000, usually finish within 10 iterations

return:
- group: a vector of length n, each element is an index of group membership
- CPCs: K orthonormal basis matrices of size p by p for each cluster
- $\mathbf F$: $\mathbf F = \mathbf B^\top \mathbf\Psi \mathbf B$
- $\text{diag}\mathbf F$: $\mathbf F = (\mathbf B^\top \mathbf\Psi \mathbf B) \circ \mathbf I$ the diagonal of matrix $\mathbf F$
- centers: Mean of each cluster
- loss: loss function for each iteration

