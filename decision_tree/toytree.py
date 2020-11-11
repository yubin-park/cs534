import numpy as np
import json

class ToyTree:

    def __init__(self,
                max_depth=2, 
                min_samples_split=2):
        self.max_depth = max_depth
        self.min_samples_split = min_samples_split
        self.tree_ = {}

    def grow(self, X, y, depth):
        n, m = X.shape
        if (n < self.min_samples_split or 
            depth == 0 or
            np.mean(y) == 1 or
            np.mean(y) == 0):
            return np.mean(y)
        j_best, s_value = self.select_split_pair(X, y)
        if j_best == -1:
            return np.mean(y)
        left_idx = X[:,j_best] <= s_value
        right_idx = X[:,j_best] > s_value
        X_left, y_left = X[left_idx,:], y[left_idx]
        X_right, y_right = X[right_idx,:], y[right_idx]
        return {"split_var": j_best,
                "split_value": s_value,
                "left": self.grow(X_left, y_left, depth-1),
                "right": self.grow(X_right, y_right, depth-1)}
            
    def select_split_pair(self, X, y):
        def get_information(p):
            if p == 0 or p == 1:
                return 0
            else:
                return -(p * np.log2(p) + (1-p) * np.log2(1-p))

        n, m = X.shape
        split_var = -1
        split_val = -1
        max_info_gain = -np.inf
        for j in range(m):
            for v in np.unique(X[:,j]):
                left_idx = X[:,j] <= v
                right_idx = X[:,j] > v
                left_size = np.sum(left_idx)
                right_size = np.sum(right_idx)
                if left_size == 0 or right_size == 0:
                    continue
                left_p = np.mean(y[left_idx])
                right_p = np.mean(y[right_idx])
                left_info = get_information(left_p)
                right_info = get_information(right_p)
                info_gain = -(left_size/n * left_info + 
                            right_size/n * right_info)
                if info_gain > max_info_gain:
                    max_info_gain = info_gain
                    split_var = j
                    split_val = v
        return split_var, split_val

    def fit(self, X, y):
        self.tree_ = self.grow(X, y, self.max_depth)

    def predict(self, X):
        # TODO: how would you traverse the tree to get the prediction?
        pass

if __name__=="__main__":

    from sklearn.datasets import load_iris
    from sklearn.datasets import load_breast_cancer

    X, y = load_breast_cancer(return_X_y=True)
    y = np.asarray(y == 0, dtype=int)

    tree = ToyTree(max_depth=3)
    tree.fit(X, y)

    print(json.dumps(tree.tree_, indent=2))
    #print(y[X[:,2] <= 1.9])
    #print(y[X[:,2] > 1.9])
        

