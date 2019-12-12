import numpy as np

class MeanRegressor:
    def __init__(self):
        self.y_mean = 0
    
    def fit(self, X, y):
        self.y_mean = np.mean(y)
    
    def predict(self, X):
        rows = X.shape[0]
        mean_values = [self.y_mean]*rows

        return np.array(mean_values)
    
    def score(self, X, y):
        tot_RSS = (y - self.predict(X))**2
        tot_TSS = (y - np.mean(y))**2
        R = 1 - (np.sum(tot_RSS)) / (np.sum(tot_TSS))
        # print(R)
        # print(1 - (np.sum(tot_RSS)))
        # print(np.sum(tot_TSS))
        return R

        #  tot_RSS = 0
        #  tot_TSS = 0
        #  X_mean = predict(X)
        # y - pre


        #  for index, value in enumerate(y):
        #      tot_RSS = tot_RSS + (value - predict(X))**2

         
        #  (y - predict(X)) / (y - self.y_mean)