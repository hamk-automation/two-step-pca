Help on module two_step_pca:

NAME
    two_step_pca

CLASSES
    builtins.object
        TS_PCA
    
    class TS_PCA(builtins.object)
     |  Methods defined here:
     |  
     |  detect(self, data, var_explained)
     |      Uses pretrained TS-PCA model to obtain Hotelling's T2 and SPE metrics for the test data
     |      Arguments:
     |          data - pandas dataframe or numpy array, testing data 
     |          var_explained - float (0-1), determines how many principal components are used for T2 and SPE calculations
     |                          rule of the thumb, keep it around 0.8-0.9
     |      Returns:
     |          metrics_df - pandas dataframe with T2 and SPE metrics
     |  
     |  fit(self, data, q, D)
     |      Fit TS-PCA model with training data 
     |      Arguments:
     |          data - pandas dataframe (or numpy array), training data 
     |          q - lag parameter 
     |          D - time difference parameter
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  scaler = StandardScaler(copy=True, with_mean=True, with_std=True)

FUNCTIONS
    calcA(data, lag, D)
        Calculates matrix A, which represents dynamic part of the model
        Arguments:
            data - numpy array with input data
            lag - lag parameter of the model
            D - time difference parameter
        Returns:
            A - numpy array describing dynamic part of the TS-PCA
    
    computeSPE(T)
        Computes SPE metric
        Arguments:
            T - numpy array, score matrix, unlike in Hotelling's T2 you use "m-l" PCs here,
                so T here is all principal components you didnt use in T2 calculations.
        Returns:
            SPE - numpy array, Squared Prediction Error
    
    computeT2(T, E)
        Computes T2 metric
        Arguments:
            T - numpy array, score matrix (or principal components, it is the same), usually you pick first "l" PCs, 
                which explain most variance
            E - eigenvalues which correspond to T
        Returns:
            T2 - Hotelling's T2 metric
    
    delta(data, D)
        Calculates matrix dX = X(t) - X(t-D)
        Arguments:
            data - numpy array with input data 
            D - time difference between the samples
        Returns:
            dX - numpy array
    
    dividePCs(T, E, var_explained, var_explained_required)
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
    
    pca(data)
        Usual PCA decomposition which returns all intermediate parameters
        Arguments:
            data - numpy array with input data (should be already with zero mean and unit variance)
                    most probably you want to pass U(innovation part) here
        Returns:
            T - score matrix (Principal components)
            P - loading matrix (eigenvectors)
            E - eigenvalues
            var_explained - variance explained for each principal component
    
    shift_data(data, lag)
        Creates a matrix based on input data and selected lag
        Corresponds to ~X in the paper 
        Arguments:
            data - numpy array, input matrix
            lag - interger, time lag parameter 
        Returns: 
            tildaX - numpy array, ~X from the paper


