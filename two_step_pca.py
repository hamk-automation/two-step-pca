import numpy as np 

def shift_data(data, lag):
    """
    Creates a matrix based on input data and selected lag
    Corresponds to ~X in the paper
    Arguments:
        data - numpy array with input data
        lag - time lag parameter
    Returns:
        tildaX - ~X from the paper
    """
    n_samples = data.shape[0]
    n_variables = data.shape[1]

    tildaX = np.zeros((n_samples - lag, n_variables*lag + n_variables))
    for t in range(lag, n_samples):
        for l in range(lag + 1):
            for v in range(n_variables):
                tildaX[t - lag, v + l*n_variables] = data[t - l, v]
                
    
    return tildaX

def delta(data, D):
    """
    Calculates matrix dX = X(t) - X(t-D)
    Arguments:
        data - numpy array with input data 
        D - time difference between the samples
    Returns:
        dX - numpy array
    """
    n_samples, n_variables = data.shape
    dX = np.zeros((n_samples - D, n_variables))

    for i in range(n_samples - D):
        dX[i] = data[i + D] - data[i]
    
    return dX

def calcA(data, lag, D):
    """
    Calculates matrix A, which represents dynamic part of the model
    Arguments:
        data - numpy array with input data
        lag - lag parameter of the model
        D - time difference parameter
    Returns:
        A - numpy array describing dynamic part of the TS-PCA
    """
    X = data
    tildaX = shift_data(X, lag)

    dX = delta(X, D)
    dtildaX = delta(tildaX, D)
    sizeDiff = dX.shape[0] - dtildaX.shape[0]
    dX = dX[sizeDiff:]
    A1 = np.linalg.inv(np.dot(dtildaX.T, dtildaX))
    A2 = np.dot(dtildaX.T, dX)
    A = np.dot(A1,A2)

    return A
      

def computeT2(T, E):
    """
    Computes T2 metric
    Arguments:
        T - numpy array, score matrix (or principal components, it is the same), usually you pick first "l" PCs, 
            which explain most variance
        E - eigenvalues which correspond to T
    Returns:
        T2 - Hotelling's T2 metric
    """
    T2 = np.zeros((T.shape[0], 1))
    
    for i in range(T.shape[0]):
        for k in range(T.shape[1]):
            T2[i] = (T[i, k] * T[i, k]) / E[k]
    
    return T2

def computeSPE(T):
    """
    Computes SPE metric
    Arguments:
        T - numpy array, score matrix, unlike in Hotelling's T2 you use "m-l" PCs here,
            so T here is all principal components you didnt use in T2 calculations.
    Returns:
        SPE - numpy array, Squared Prediction Error
    """
    SPE = np.zeros((T.shape[0], 1))
    for i in range(T.shape[0]):
        SPE[i] = np.sum(np.square(T[i]))

    return SPE


def fit_transform(data, q, D):
    """
    Fit TS-PCA model with data 
    Arguments:
        data - numpy array with input data
        q - lag, if not specified will use the one from constructor
        D - time difference between two data samples used for estimating dynamic part,
            if not specified the one from constructor is used
    Returns:
        U - innovation part (numpy array)
        A - numpy array describing dynamic part of the model
        tildaX - time shifted input numpy array
    """
    
    A = calcA(data, q, D)
    tildaX = shift_data(data, q)
    #shift_data reduces the size of input data by lag, so it is necessary to align dimensions
    sizeDiff = data.shape[0] - tildaX.shape[0]
    data = data[sizeDiff:]
    U = data - np.dot(tildaX, A)

    return U, A, tildaX

def pca(data):
    """
    Usual PCA decomposition which returns all intermediate parameters
    Arguments:
        data - numpy array with input data (should be already with zero mean and unit variance)
                most probably you want to pass U(innovation part) here
    Returns:
        T - score matrix (Principal components)
        P - loading matrix (eigenvectors)
        E - eigenvalues
        var_explained - variance explained for each principal component
    """
    cov_matrix = np.cov(data.T)
    eig_vals, eig_vectors = np.linalg.eig(cov_matrix)
    #the next line combines eig_vals and eig_vectors into pairs for further soring
    #numpy.linalg.eig usually returns them sorted, but it is not guaranteed
    eig_pairs = [[np.abs(eig_vals[i]), eig_vectors[:, i]] for i in range(len(eig_vals))]
    eig_pairs.sort()
    eig_pairs.reverse()
    #computing explained variance for each principal component
    var_explained = [(i/sum(eig_vals)) for i in sorted(eig_vals, reverse=True)]
    #extracting eigen vectors and eigen values from the pairs and converting them to numpy arrays,
    #because I like them better
    P = np.array([i[1] for i in eig_pairs])
    T = np.dot(data, P.T)
    E = np.array([i[0] for i in eig_pairs])

    return T, P, E, var_explained

def dividePCs(T, E, var_explained, var_explained_required):
    """
    Divides Principal component matrix into two matricies, depending on how much variance,
    must be explained. You can think of this function the same way, as n_pca (or n_components) in sklearn.decomposition.PCA
    Arguments:
        T - numpy array, score matrix
        E - numpy array, eigenvalues
        var_explained - list, consists of values, which show how much variance each PC explains
        var_explained_required - float, how much variance must be explained by all selected PCs
    Returns:
        T_l - numpy array, score matrix with top l PCs, which explain required amount of variance
        E_l - numpy array, eigen values which correspond to T_l score matrix
        T_rest - numpy array, score matrix containing all the PCs not included in T_l, it is needed for SPE calculations
    """
    total_var_explained = 0
    n_pca = 0
    for i in var_explained:
        total_var_explained = total_var_explained + i
        n_pca = n_pca + 1
        if total_var_explained >= var_explained_required:
            break

    return T[:, :n_pca], E[:n_pca], T[:, n_pca:]