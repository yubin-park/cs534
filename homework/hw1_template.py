# Please do not use other libraries except for numpy
import numpy as np


class Ridge:

    def __init__(self):
        self.intercept = 0
        self.coef = None

    def fit(self, X, y, coef_prior=None, lmbd=1.0):

        n, m = X.shape
        self.coef = np.zeros(m)
        if coef_prior == None:
            coef_prior = np.zeros(m)

        # a) normalize X
        x_mu = 
        x_sigma = ...
        X = ... # normalized X

        # b) adjust coef_prior according to the normalization parameters
        coef_prior = ...

        # c) get coefficients
        ...
        self.intercept = ...
        self.coef = ...

        # d) adjust coefficients for de-normalized X
        self.intercept = ... 
        self.coef = ...

        return 0

    def get_coef(self):
        return self.intercept, self.coef

class ForwardStagewise:

    def __init__(self):
        self.intercept = 0
        self.path = []

    def fit(self, X, y, cannot_link=[], epsilon=1e-5, max_iter=1000):

        # a) normalize X

        # b-1) implement incremental forwward-stagewise
        # b-2) implement cannot-link constraints

        # c) adjust coefficients for de-normalized X

        # d) construct the "path" numpy array
        #     path: l-by-m array,
        #               where l is the total number of iterations
        #               m is the number of features in X.
        #               The first row, path[0,:], should be all zeros.

        return 0

    def get_coef_path(self):
        return self.intercept, self.path



